import requests
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self) -> None:
        for result in self.query({'action':'query','list':'categorymembers','cmtitle':'Category:English_idioms', 'cmprop':'title','cmlimit':'max'}):
            print(result)

    def query(self, request):
        request['action'] = 'query'
        request['format'] = 'json'
        last_continue = {}
        while True:
            req = request.copy()
            req.update(last_continue)
            result = requests.get('https://en.wiktionary.org/w/api.php',params=req).json()
            if 'error' in result:
                raise Exception(result['error'])
            if 'warnings' in result:
                print(result['warnings'])
            if 'query' in result:
                yield result['query']
            if 'continue' not in result:
                break
            last_continue = result['continue']


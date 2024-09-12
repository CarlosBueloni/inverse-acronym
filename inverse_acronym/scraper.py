import requests
from unidecode import unidecode

class Scraper():
    def __init__(self, category_title) -> None:
        self._category_title = category_title
        self._dict = {}

    def get_requests(self):
        for result in self.query({'list':'categorymembers','cmtitle':f'Category:{self._category_title}', 'cmprop':'title','cmlimit':'max'}):
            print('loading...')
            for member in result['categorymembers']:
                initials = unidecode(self._get_initials(member['title']).lower())
                self._dict[initials] = member['title']
        
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

    def _get_initials(self, text):
        return ''.join([word[0] for word in text.split()])

    def get_results(self, acronym):
        if acronym in self._dict:
            return self._dict[acronym]
        else:
            return "I'm sorry please try another acronym"

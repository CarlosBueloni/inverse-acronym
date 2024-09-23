import requests
from unidecode import unidecode

class Data():
    def __init__(self) -> None:
        self._dict = {}

    def get_requests(self, category):
        for result in self.query({'list':'categorymembers','cmtitle':f'Category:{category}', 'cmprop':'title','cmlimit':'max'}):
            print('loading...')
            if category not in self._dict:
                self._dict[category] = {}
            for member in result['categorymembers']:
                initials = unidecode(self._get_initials(member['title']).lower())
                if member['title'].startswith("Appendix:") or member['title'].startswith("Category:"):
                    continue
                if initials in self._dict[category]:
                    self._dict[category][initials].append(member['title'])
                else:
                    self._dict[category][initials] = [member['title']]

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
        results = []
        for category in self._dict.keys():
            if acronym in self._dict[category]:
                results.extend(self._dict[category][acronym])
        return results

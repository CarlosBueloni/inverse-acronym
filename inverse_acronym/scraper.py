import requests
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self._r = None
        self._soup = None


    def get_html(self, url):
        self._r = requests.get(url)
        self._soup = BeautifulSoup(self._r.content, "html.parser")
        self._search_idioms()

    def _search_idioms(self):
        if self._soup is not None:
            idioms = self._soup.find("div", class_="mw-category mw-category-columns")
            for idiom in idioms.find_all("li"):
                print(idiom.get_text())

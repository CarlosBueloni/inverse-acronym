import re, requests
from bs4 import BeautifulSoup as bs

class parser(object):
    def __init__(self):
        self.url = "https://en.wiktionary.org/wiki/{}?printable=yes"
        self.soup = None
        self.session = requests.Session()
    

    def parse_next_page_links(self, category):
        link_tags = self.soup.find('div', {'id': 'mw-pages'}).find_all('a', {'title': category})
        return [link['href'] for link in link_tags if link.text == 'next page']

    def parse_category_words(self):
        words_content = self.soup.find('div', {'id': 'mw-pages'}).find('div', {'class': 'mw-content-ltr'})
        words = [word.text for word in words_content.find_all('a')]
        print(words)
        return words

    def get_category_data(self, category):
        words = []
        next_page_links = self.parse_next_page_links(category)
        while len(next_page_links) > 0:
            words += self.parse_category_words()
            response = self.session.get('https://en.wiktionary.org/' + next_page_links[0])
            self.soup = bs(response.text.replace('>\n<', '><'), 'html.parser')
            self.clean_html()
            next_page_links = self.parse_next_page_links(category)
        words += self.parse_category_words()

    def fetch_category(self, category):
        category = "Category:" + category
        self.response = self.session.get(self.url.format(category))
        self.soup = bs(self.response.text.replace('>\n', '><'), 'html.parser')
        self.clean_html()
        return self.get_category_data(category)


    def clean_html(self):
            unwanted_classes = ['sister-wikipedia', 'thumb', 'reference', 'cited-source']
            for tag in self.soup.find_all(True, {'class': unwanted_classes}):
                tag.extract()




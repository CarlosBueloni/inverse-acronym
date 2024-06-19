from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
source = urlopen('https://en.wiktionary.org/w/index.php?title=Category:English_idioms&from=A').read()

# Make a soup 
soup = BeautifulSoup(source,'lxml')
soup

# Extract the plain text content from paragraphs
text = soup.find(attrs = {"class", 'mw-category mw-category-columns'}).text
phrases= []
# Extract text from paragraph headers
for phrase in text.split('\n'):
    phrases.append(phrase.split())

def get_initials(phrase):
    return ''.join([word[0].lower() for word in phrase])

def search_for_phrase(initials):
    for phrase in phrases:
        if get_initials(phrase) == initials:
            return ' '.join(phrase)

    return 'Phrase for acronym not found'

print(search_for_phrase('ab'))

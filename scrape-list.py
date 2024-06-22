from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, requests
from parser import parser

# Specify url of the web page

# Make a soup 
# soup = BeautifulSoup(source,'lxml')


# Extract the plain text content from paragraphs
#text = soup.find(attrs = {"class", 'mw-category mw-category-columns'}).text
#phrases= []
# Extract text from paragraph headers
#for phrase in text.split('\n'):
#    phrases.append(phrase.split())
#
#def get_initials(phrase):
#    return ''.join([word[0].lower() for word in phrase])

def search_for_phrase(initials):
    for phrase in parser().fetch_category("English idioms"):
        if get_initials(phrase) == initials:
            return ' '.join(phrase)
print(parser().fetch_category("English idioms"))
#    return 'Phrase for acronym not found'

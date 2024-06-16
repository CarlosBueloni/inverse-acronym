from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
source = urlopen('https://en.wiktionary.org/wiki/Category:English_idioms').read()

# Make a soup 
soup = BeautifulSoup(source,'lxml')
soup

# Extract the plain text content from paragraphs
phrases = []
for phrase in soup.find_all('div', class_='mw-category-group'):
    print(phrase.text)
# Extract text from paragraph headers



print(phrases)


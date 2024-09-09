from scraper import Scraper

def main():
    acronym = input("Enter the acronym: ")
    new_scraper = Scraper()
    new_scraper.get_html("https://en.wiktionary.org/w/index.php?title=Category:English_idioms&from=A")

if __name__ == "__main__":
    main()

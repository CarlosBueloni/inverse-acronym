from scraper import Scraper

def main():
    #acronym = input("Enter the acronym: ")
    new_scraper = Scraper('English_idioms')
    new_scraper.get_requests()


if __name__ == "__main__":
    main()

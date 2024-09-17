from data import Data

def main():
    category = input("Enter the category: ")
    new_scraper = Scraper(category)
    new_scraper.get_requests()
    acronym = input("Enter the acronym (type 0 to close): ")
    while acronym != '0':
        print(new_scraper.get_results(acronym))
        acronym = input("Enter the acronym (type 0 to close): ")



if __name__ == "__main__":
    main()

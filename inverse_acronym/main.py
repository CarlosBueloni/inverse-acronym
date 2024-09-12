from scraper import Scraper

def main():
    category = input("Enter the category: ")
    new_scraper = Scraper(category)
    new_scraper.get_requests()
    while True:
        acronym = input("Enter the acronym: ")
        print(new_scraper.get_results(acronym))



if __name__ == "__main__":
    main()

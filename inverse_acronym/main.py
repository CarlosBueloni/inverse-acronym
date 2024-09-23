from data import Data

def main():
    data = Data()
    category = input("Enter the category: ")
    while category != '0':
        data.get_requests(category)
        category = input("Enter the category (type 0 to continue): ")
    acronym = input("Enter the acronym (type 0 to close): ")
    while acronym != '0':
        print(data.get_results(acronym))
        acronym = input("Enter the acronym (type 0 to close): ")



if __name__ == "__main__":
    main()

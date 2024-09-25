class Menus():
    def __init__(self,data) -> None:
        self.data = data
        self.main = """
    1- Select Category
    2- Check Categories
    3- Search Acronym
    4- Exit
    """
        self.category = "Please type a category (0 to go back): "
        self.delete_category = "Please select a category to delete or 0 to go back): "
        self.acronym = "Please type an acronym (type 0 to go back): "


    def main_selection(self):
        print(self.main)
        option = input("Choose an option: ")
        if option == '1':
            self.select_category()
        if option == '2':
            self.check_categories()
        if option == '3':
            self.search_acronym()
        if option == '4':
            return
    
    def select_category(self):
        while True:
            print("")
            category = input(self.category)
            if category == '0':
                break
            self.data.get_requests(category)

        self.main_selection()
        return


    def check_categories(self):
        while True:
            print("")
            categories = self.data.get_categories()
            if len(categories) == 0:
                break
            for i, category in enumerate(categories):
                print(f"{i+1} - {category}")
            option = input(self.delete_category)
            if option == '0':
                break
            self.data.delete_category(categories[int(option)-1])
        self.main_selection()
        return


    def search_acronym(self):
        while True:
            print("")
            acronym = input(self.acronym)
            if acronym == '0':
                break
            results = self.data.get_results(acronym)
            if len(results) > 0:
                for i, result in enumerate(results):
                    print(f"{i+1} - {result}")
            else:
                print("Sorry please enter another acronym")
        self.main_selection()
        return


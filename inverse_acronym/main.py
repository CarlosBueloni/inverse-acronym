from data import Data
from menus import Menus

def main():
    data = Data()
    menu = Menus(data)
    menu.main_selection()
    


if __name__ == "__main__":
    main()

from Library import Library

class main:

    lib = Library()

    def print_menu():
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Quit")

    while True:
        print()
        print_menu()
        option = input("Enter your choice (1,2,3,q): ")

        if option==("1"):
            lib.list_books()

        elif option == ("2"):
            lib.add_book()

        elif option == ("3"):
            lib.remove_book()

        elif option==("q"):
            break

        else:
            print("Invalid option.Please try again.")






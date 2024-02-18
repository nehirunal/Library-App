
class Library:

    def __init__(self):
        self.file = open("book.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            print("List of Books:")
            for book in books:
                book_info = book.split(',')
                book_name = book_info[0]
                author = book_info[1]
                print(f"Book: {book_name}, Author: {author}")
    def add_book(self):
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            release_year = input("Enter the release year of the book: ")
            num_pages = input("Enter the number of pages of the book: ")

            book_info = f"{title},{author},{release_year},{num_pages}\n"
            self.file.write(book_info)
            print(f"'{title}' added successfully.")

    def remove_book(self):

            title = input("Enter the title of the book you want to remove: ")
            books = []

            self.file.seek(0)
            for line in self.file:
                if title not in line:
                    books.append(line)

            self.file.seek(0)
            self.file.truncate()

            for book in books:
                self.file.write(book)

            print(f"'{title}' removed successfully.")








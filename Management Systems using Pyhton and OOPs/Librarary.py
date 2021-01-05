class Library:
    def __init__(self, list_of_books, Library_name):
        # Creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # Adding books to dictionary
        for books in self.list_of_books:
            # none means No reader have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    # By default variables
    list_books = ['Cookbook', 'Sherlock Holmes', 'Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    Harry = Library(list_books, Library_name)

    print(
        f"Welcome To {Harry.library_name} library\nQuit for exit \nDisplay Book Using 'Display' and add lend book using 'Lend' and Return a Book using 'Return_a_book' \nAdd Book Using 'Add_books' and Delete Book using 'Delete_a_book' \n ")

    Exit = True
    while Exit:
        _input = input("option:")
        print("\n")

        if _input == "Quit":
            Exit = False

        elif _input == "Display":
            Harry.display_books()

        elif _input == "Lend":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("Book Lend\n")
            Harry.lend_book(_input3, _input2)
            print('You want to do anything else then type More options and if you want to leave then type Quit')
            a = input('option:')
            if a == 'More Options':
                continue
            elif a == 'Quit':
                Exit = False
                continue
            continue

        elif _input == "Add_books":
            _input2 = input("Book name:")
            Harry.add_book(_input2)

        elif _input == "Delete_a_book":
            _input_secret = int(input("Write the secret key to delete:"))
            if _input_secret == secret_key:
                _input2 = input("Book Which you want to delete:")
                Harry.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "Return_a_book":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Harry.return_book(_input3, _input2)
            print('Thank You returning the book')


if __name__ == "__main__":
    main()

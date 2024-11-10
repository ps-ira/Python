class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booklist:
            print("Sorry, the book is not available in our library.")
        elif book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print(f"Lender-book database has been updated. {user} can now take the book.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the booklist")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"The book '{book}' has been successfully returned.")
        else:
            print(f"Sorry, the book '{book}' was not lent out.")

if __name__ == '__main__':
    books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")

    while True:
        print(f"Welcome to the {books.name} library. Enter your choice to continue")

        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)

        print("Press 'q' to quit and 'c' to continue")
        user_choice2 = ""

        while user_choice2 not in ["c", "q"]:
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue

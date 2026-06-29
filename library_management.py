class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found:")
                print(book)
                return
        print("Book not found.")

    def update_book(self, old_title, new_title, new_author):
        for book in self.books:
            if book.title.lower() == old_title.lower():
                book.title = new_title
                book.author = new_author
                print("Book updated successfully!")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        title = input("Enter book title to remove: ")
        library.remove_book(title)

    elif choice == "3":
        title = input("Enter book title to search: ")
        library.search_book(title)

    elif choice == "4":
        old_title = input("Enter current book title: ")
        new_title = input("Enter new title: ")
        new_author = input("Enter new author: ")
        library.update_book(old_title, new_title, new_author)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
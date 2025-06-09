class Book:
    def __init__(self, title, author, isbn, available_copies):
        """Constructor for creating new book objects"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        """Displays the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.available_copies}")

    def borrow_book(self):
        """Decrements the number of available copies if the book is available."""
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"'{self.title}' has been borrowed successfully.")
            return True
        else:
            print(f"Sorry, '{self.title}' is currently out of stock.")
            return False

    def return_book(self):
        """Increments the number of available copies when a book is returned."""
        self.available_copies += 1
        print(f"'{self.title}' has been returned successfully.")


class Library:
    def __init__(self):
        self.books = []  # library of books

    def add_book(self, book):
        """Adds a new book to the library."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def find_book_by_title(self, title):
        """Searches for a book by its title and returns the book object if found."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_all_books(self):
        """Displays details of all books in the library."""
        if not self.books:
            print("The library currently has no books.")
        else:
            print("\n--- All Books in the Library ---")
            for book in self.books:
                book.display_info()
                print("-" * 30)


# Demonstrate the functionality
if __name__ == "__main__":
    # Create a few Book objects
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 3)
    book2 = Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 5)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789", 3)

    # Create a Library object
    my_library = Library()

    # Add books to the Library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Display all books in the library
    my_library.display_all_books()

    # Borrow and return books, and display their updated status
    print("\n--- Borrowing and Returning Books ---")
    book1.borrow_book()
    book1.display_info()
    print("-" * 30)

    book3.borrow_book()
    book3.borrow_book()
    book3.borrow_book()  # Attempt to borrow more than available
    book3.display_info()
    print("-" * 30)

    book1.return_book()
    book1.display_info()
    print("-" * 30)

    # Search for a book by title and display its details
    print("\n--- Searching for Books ---")
    found_book = my_library.find_book_by_title("Pride and Prejudice")
    if found_book:
        print("Book found:")
        found_book.display_info()
    else:
        print("Book not found.")
    print("-" * 30)

    found_book_nonexistent = my_library.find_book_by_title("Moby Dick")
    if found_book_nonexistent:
        print("Book found:")
        found_book_nonexistent.display_info()
    else:
        print("Book 'Moby Dick' not found.")
    print("-" * 30)

    # Display all books again to see the updated availability
    my_library.display_all_books()
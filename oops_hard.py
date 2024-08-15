# Implement classes for Book, Member, Librarian, and Library.
# Book should have attributes like title, author, ISBN, and status.
# Member should have attributes like name, member_id, and a list of borrowed books.
# Librarian should have attributes like name and employee_id.
# Library should have a collection of books and methods to add/remove books, register members, lend books, and return books.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'

    def borrow(self):
        self.status = 'borrowed'

    def return_book(self):
        self.status = 'available'


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == 'available':
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")


class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.title} from the library.")
        else:
            print(f"{book.title} is not in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}.")

    def lend_book(self, member_id, isbn):
        member = None
        book = None
        
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if member and book:
            member.borrow_book(book)
        else:
            print("Member or book not found.")

    def return_book(self, member_id, isbn):
        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if member and book:
            member.return_book(book)
        else:
            print("Member or book not found.")



def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Register a Member")
        print("4. Lend a Book")
        print("5. Return a Book")
        print("6. View All Books")
        print("7. View All Members")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter the book ISBN to remove: ")
            book = next((b for b in library.books if b.isbn == isbn), None)
            if book:
                library.remove_book(book)
            else:
                print("Book not found.")

        elif choice == '3':
            name = input("Enter the member name: ")
            member_id = input("Enter the member ID: ")
            member = Member(name, member_id)
            library.register_member(member)

        elif choice == '4':
            member_id = input("Enter the member ID: ")
            isbn = input("Enter the book ISBN to lend: ")
            library.lend_book(member_id, isbn)

        elif choice == '5':
            member_id = input("Enter the member ID: ")
            isbn = input("Enter the book ISBN to return: ")
            library.return_book(member_id, isbn)

        elif choice == '6':
            print("\nLibrary Books:")
            for book in library.books:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - Status: {book.status}")
            if not library.books:
                print("No books in the library.")

        elif choice == '7':
            print("\nLibrary Members:")
            for member in library.members:
                borrowed_titles = ", ".join([book.title for book in member.borrowed_books])
                print(f"Member: {member.name} (ID: {member.member_id}) - Borrowed Books: {borrowed_titles if borrowed_titles else 'No books borrowed'}")
            if not library.members:
                print("No members registered.")


        elif choice == '8':
                print("Exiting the Library System. Goodbye!")
                break

        else:
            print("Invalid choice. Please try again.")
main()


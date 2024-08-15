# 1. Implement classes for Book, Member, Librarian, and Library.
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


# 2. Implement classes for Account, SavingsAccount, CheckingAccount, and Bank.
# Account should be a base class with attributes like account_number, balance, and methods for deposit and withdraw.
# SavingsAccount should inherit from Account and add an attribute for interest rate.
# CheckingAccount should inherit from Account and add an attribute for overdraft limit.
# Bank should manage multiple accounts and provide methods to create accounts, transfer money, and generate account statements.

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        Account.__init__(self, account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return (f"Savings Account\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: {self.balance}\n"
                f"Interest Rate: {self.interest_rate * 100}%")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        return self.balance

    def __str__(self):
        return (f"Checking Account\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: {self.balance}\n"
                f"Overdraft Limit: {self.overdraft_limit}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_savings_account(self, account_number, balance=0, interest_rate=0.01):
        self.accounts[account_number] = SavingsAccount(account_number, balance, interest_rate)

    def create_checking_account(self, account_number, balance=0, overdraft_limit=500):
        self.accounts[account_number] = CheckingAccount(account_number, balance, overdraft_limit)

    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if from_account.withdraw(amount) >= 0:
                to_account.deposit(amount)

    def generate_statement(self, account_number):
        account = self.accounts.get(account_number)
        return str(account) if account else "Account not found."


def main():
    bank = Bank()
    
    while True:
        print("\nBank Menu:")
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Apply Interest to Savings Account")
        print("7. Generate Account Statement")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate (as a decimal): "))
            bank.create_savings_account(account_number, balance, interest_rate)
            print(f"Savings account {account_number} created.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            bank.create_checking_account(account_number, balance, overdraft_limit)
            print(f"Checking account {account_number} created.")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.accounts.get(account_number)
            if account:
                account.deposit(amount)
                print(f"Deposited {amount} into account {account_number}.")
            else:
                print("Account not found.")
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.accounts.get(account_number)
            if account:
                if account.withdraw(amount) >= 0:
                    print(f"Withdrew {amount} from account {account_number}.")
                else:
                    print("Insufficient funds or overdraft limit exceeded.")
            else:
                print("Account not found.")
        
        elif choice == '5':
            from_account_number = input("Enter sender account number: ")
            to_account_number = input("Enter receiver account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer_money(from_account_number, to_account_number, amount)
            print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}.")
        
        elif choice == '6':
            account_number = input("Enter savings account number: ")
            account = bank.accounts.get(account_number)
            if isinstance(account, SavingsAccount):
                account.apply_interest()
                print(f"Applied interest to account {account_number}. New balance: {account.balance}")
            else:
                print("Savings account not found.")
        
        elif choice == '7':
            account_number = input("Enter account number: ")
            print(bank.generate_statement(account_number))
        
        elif choice == '8':
            print("Exiting the banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()

# 3. Implement classes for Person, Student, Teacher, Course, and School.
# Person should be a base class with attributes like name and age.
# Student and Teacher should inherit from Person and add specific attributes/methods.
# Course should have attributes like course_id, name, and students.
# School should manage students, teachers, and courses, and provide methods to enroll students, assign teachers, and generate reports on courses.
# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        self.name = name
        self.age = age
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        course.assign_teacher(self)

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def enroll_student(self, student):
        self.students.append(student)

    def hire_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = None
        course = None

        for t in self.teachers:
            if t.teacher_id == teacher_id:
                teacher = t
                break

        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break

        if teacher and course:
            teacher.assign_course(course)
            course.assign_teacher(teacher)

    def generate_course_report(self):
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Name: {course.name}")
            if course.teacher:
                print(f"  Teacher: {course.teacher.name}")
            else:
                print("  No teacher assigned yet.")
            print("  Enrolled Students:")
            for student in course.students:
                print(f"    {student.student_id}: {student.name}")
            print()

def main():
    school = School("XYZ public school")
    while True:
        print("\nSchool Management System")
        print("1. Enroll Student")
        print("2. Hire Teacher")
        print("3. Add Course")
        print("4. Assign Teacher to Course")
        print("5. Enroll Student in Course")
        print("6. Generate Course Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student_id = input("Enter student ID: ")
            student = Student(name, age, student_id)
            school.enroll_student(student)
            print(f"Student {name} enrolled successfully.")

        elif choice == "2":
            name = input("Enter teacher name: ")
            age = int(input("Enter teacher age: "))
            teacher_id = input("Enter teacher ID: ")
            teacher = Teacher(name, age, teacher_id)
            school.hire_teacher(teacher)
            print(f"Teacher {name} hired successfully.")

        elif choice == "3":
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            school.add_course(course)
            print(f"Course {name} added successfully.")

        elif choice == "4":
            teacher_id = input("Enter teacher ID: ")
            course_id = input("Enter course ID: ")
            school.assign_teacher_to_course(teacher_id, course_id)
            print("Teacher assigned to course successfully.")

        elif choice == "5":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")

            student = None
            course = None

            for s in school.students:
                if s.student_id == student_id:
                    student = s
                    break

            for c in school.courses:
                if c.course_id == course_id:
                    course = c
                    break

            if student and course:
                student.enroll_in_course(course)
                print("Student enrolled in course successfully.")
            else:
                print("Invalid student ID or course ID.")

        elif choice == "6":
            school.generate_course_report()

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

main()

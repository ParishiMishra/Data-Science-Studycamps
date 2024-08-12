#1.  Write a Python program to create a person class. 
# Include attributes  like name, country and date of birth.
# Implement a method to  determine the person’s age. 
from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    def calculateage(self):
        today = date.today()
        birthdate=self.dob
        age=today.year-birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
def main():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    dateofbirth = input("Enter your date of birth (yyyy,mm,dd): ")
    year, month, day = map(int, dateofbirth.split(','))
    dob = date(year, month, day)
    person = Person(name, country, dob)
    print("Name: ", person.name)
    print("Country: ", person.country)
    print("Age: ", person.calculateage())
main()

#2. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")
        return self.balance
    
def main():
    name = input("Enter name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, name, balance)
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.get_balance()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        ans=input("Do you want to continue? y/n: ")
        if ans=='n':
            break
main()
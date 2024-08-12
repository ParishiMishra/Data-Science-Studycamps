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
#main()

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
#main()

# 3. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price. 
class shoppingcart:
    def __init__(self):
        self.items=[]
    def add_item(self,name,price, quantity):
        item ={
            'name':name,
            'price':price,
            'quantity':quantity
        }
        self.items.append(item)
        print(f"Added {quantity} x {name}(s) to the cart.")

    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                print(f"Removed {name} from the cart.")
                return
        print(f"Item {name} not found in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def display_cart(self):
        if len(self.items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("Your shopping cart contains:")
            for item in self.items:
                print(f"{item['quantity']} x {item['name']} @ ${item['price']:.2f} each")
            print(f"Total price: ${self.calculate_total():.2f}")

def main():
    cart = shoppingcart()
    cart.add_item("Apple", 0.99, 3)
    cart.add_item("Banana", 0.59, 5)
    cart.add_item("Orange", 0.79, 2)
    cart.display_cart()
    cart.remove_item("Banana")
    cart.display_cart()
    total_price = cart.calculate_total()
    print(f"The total price of the items in the cart is: ${total_price:.2f}")
#main()
    
#4. Write a Python program to create a calculator class. 
# Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        else:
            return a / b
def main():
    calculator = Calculator()
    num1=eval(input("Enter num1: "))
    num2=eval(input("Enter num2: "))
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Choose an operation (1-5): ")
        if choice == '1':
            print(f"Result: {calculator.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {calculator.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {calculator.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {calculator.divide(num1, num2)}")
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please choose a valid operation.")
        ans=input("Do you want to continue? y/n: ")
        if ans=='n':
            break
main()
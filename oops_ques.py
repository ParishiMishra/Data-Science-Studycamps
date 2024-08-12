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
'''10. OOP Basics
46. Create a Student class with name and marks, and a method to print details.
47. Implement inheritance: a Person class and a Student subclass.
48. Use __init__ and __str__ magic methods.
49. Create a class with a class variable vs instance variable.
50. Implement a simple BankAccount class with deposit/withdraw methods.
'''

#46. Create a Student class with name and marks, and a method to print details.
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_info(self):
        print(self.name,self.marks)

students=student("Mahi",90)
students.get_info()

#47. Implement inheritance: a Person class and a Student subclass.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print(self.name,self.age)

class student(person):
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def get_info(self):
        print(self.name,self.age,self.marks)

students=student("Mahi",20,90)
students.get_info()

#48. Use __init__ and __str__ magic methods.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=student("Mahi",20)
print(student1.age)

#49. Create a class with a class variable vs instance variable.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print(self.name,self.age)

students=student("Mahi",20)
students.get_info()

#50. Implement a simple BankAccount class with deposit/withdraw methods.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def get_info(self):
        print(self.name,self.balance)

bankaccount=BankAccount("Mahi",1000)
bankaccount.deposit(100)
bankaccount.withdraw(100)
bankaccount.get_info()

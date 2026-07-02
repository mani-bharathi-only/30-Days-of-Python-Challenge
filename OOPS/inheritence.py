#Inheritance
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog=Dog("Joe")
cat=Cat("Julie")
cat.eat()


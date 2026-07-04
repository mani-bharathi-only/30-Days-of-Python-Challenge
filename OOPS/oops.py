#Classes and Objects

from classes import Car

ca1=Car("BMW","Red",2026)

print(ca1.name)
print(ca1.color)
print(ca1.year)

ca1.start()


#Class variable and Instance variable
class stud:

    school="Joseph"   #class variable

    def __init__(self,name,classs,age):  #constructor
        self.name=name      #instance variable
        self.classs=classs
        self.age=age

Student1=stud("Vinoth","3rd","7")
print(Student1.age)
print(Student1.name)
print(Student1.classs)

print(stud.school)


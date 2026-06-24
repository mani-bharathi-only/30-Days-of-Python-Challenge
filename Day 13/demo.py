#Python Closure
def num():
    five=5
    def value(n):
        return five + n
    return value
jk=num()
print(jk(2))

#Without using Decorator 
def func():
    return "Ok Google"
def return_val(function):
    def upp():
        nm=function()
        new=nm.upper()
        return new
    return upp
k=return_val(func)
print(k())


#With Decorator
def upper_case(function1):
    def ne():
        host=function1()
        new=host.upper()
        return new
    return ne

@upper_case
def na():
    return "Hello Bro"
print(na())

def decorator(function):
    def news(para1,para2,para3):
        function(para1,para2,para3)
        return("I live in {}".format(para3))
    return  news

@decorator
def sem(firstname,lastname,country):
    print("My name is {}{}".format(firstname,lastname))
print(sem("Mani","Bharathi","Madurai"))


#Map Function with Lambda
numbers=[1,2,3,4,5]
numbered=map(lambda x:x**2,numbers)
print(list(numbered))

#Filter Function
number=[3,21,5,3,4,32,34,56,78,98,76]
def num(value):
    if value%2==0:
        return True
    return False
val=filter(num,number)
print(list(val))
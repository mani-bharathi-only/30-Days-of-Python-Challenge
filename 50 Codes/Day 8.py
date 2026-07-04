'''8. Functions
36. Write a function to check if a number is prime.
37. Write a recursive function for factorial.
38. Write a function with default and keyword arguments.
39. Write a function that returns multiple values.
40. Write a function using *args and **kwargs.'''

#36. Write a function to check if a number is prime.
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(10))

#37. Write a recursive function for factorial.
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#38. Write a function with default and keyword arguments.
def greet(name,greeting="Vanakkam"):
    print(greeting,name)
greet("Raj")
greet("Raj",greeting="Hello")

#39. Write a function that returns multiple values.
def add_sub(a,b):
    return a+b,a-b
print(add_sub(10,5))

#40. Write a function using *args and **kwargs.
def display_info(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)
display_info(1, 2, 3, name="Raj", age=25)


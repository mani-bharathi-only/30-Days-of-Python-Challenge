'''
#1. Variables & I/O

1.Take user input and print a greeting.
2.Swap two variables without a temp variable.
3.Convert Celsius to Fahrenheit.
4.Calculate simple interest given principal, rate, time.
5.Print the type of different variables (int, float, str, bool).'''

#1.Take user input and print a greeting.
from time import time
name=input("Enter your name: ")
print("Welcome",name)

#2.Swap two variables without a temp variable
a=5
b=2
a,b=b,a
print(f"a = {a},b={b}")

#3.Convert Celsius to Fahrenheit
cel=int(input("Enter the Celcius: "))
F=cel*(1.8)+32
print(f"The farenheit is {F}")

#4.Simple Interest
principle=int(input("Enter Principle: "))
rate=int(input("Enter the rate: "))
tiem=int(input("Enter the time: "))
SI=principle*rate*tiem/100
print(f"The Simple Interest is {SI}")

#5.Print the type of different variables (int, float, str, bool)
integer=int(input("Enter the Integer: "))
Float=float(input("Enter the Float Value: "))
String=str(input("Enter the Value of String: "))
Boolean=bool(input("Enter the Value of boolean: "))
print("Integer",type(integer))
print("Float",type(Float))
print("String",type(String))
print("Boolean",type(Boolean))


'''
1. Variables & I/O

Take user input and print a greeting.
Swap two variables without a temp variable.
Convert Celsius to Fahrenheit.
Calculate simple interest given principal, rate, time.
Print the type of different variables (int, float, str, bool).

2. Conditionals
6. Check if a number is even or odd.
7. Find the largest of three numbers.
8. Check if a year is a leap year.
9. Simple calculator (add/sub/mul/div based on user choice).
10. Grade calculator (marks → A/B/C/F).

3. Loops
11. Print the multiplication table of a number.
12. Sum of first N natural numbers.
13. Print the Fibonacci series up to N terms.
14. Check if a number is prime.
15. Print all prime numbers up to N.

4. Strings
16. Reverse a string.
17. Check if a string is a palindrome.
18. Count vowels in a string.
19. Count occurrences of each character (frequency dict).
20. Capitalize the first letter of every word.

5. Lists
21. Find the maximum and minimum in a list without built-ins.
22. Remove duplicates from a list.
23. Find the sum and average of a list.
24. Reverse a list in place.
25. Find the second largest element.

6. Tuples & Sets
26. Convert a list to a tuple and access elements.
27. Find the intersection and union of two sets.
28. Check membership in a set vs a list (and why sets are faster).
29. Count unique elements in a list using a set.
30. Merge two dictionaries into one.

7. Dictionaries
31. Count word frequency in a sentence.
32. Find the key with the maximum value in a dict.
33. Invert a dictionary (swap keys and values).
34. Sort a dictionary by value.
35. Group a list of words by their first letter.

8. Functions
36. Write a function to check if a number is prime.
37. Write a recursive function for factorial.
38. Write a function with default and keyword arguments.
39. Write a function that returns multiple values.
40. Write a function using *args and **kwargs.

9. File Handling
41. Write and read a text file.
42. Count the number of lines/words in a file.
43. Append data to an existing file.
44. Read a CSV file using the csv module.
45. Handle a file-not-found error using try/except.

10. OOP Basics
46. Create a Student class with name and marks, and a method to print details.
47. Implement inheritance: a Person class and a Student subclass.
48. Use __init__ and __str__ magic methods.
49. Create a class with a class variable vs instance variable.
50. Implement a simple BankAccount class with deposit/withdraw methods.
'''

'''4. Strings
16. Reverse a string.
17. Check if a string is a palindrome.
18. Count vowels in a string.
19. Count occurrences of each character (frequency dict).
20. Capitalize the first letter of every word.'''

#16. Reverse a string.
n=input("Enter the string: ")
print(n[::-1])

#17. Check if a string is a palindrome.
n1=input("Enter a string2: ")
print(n1==n1[::-1])

#18. Count vowels in a string.
n2=input("Enter a string3: ")
a=(n2.count("a"))
b=(n2.count("e"))
c=(n2.count("i"))
d=(n2.count("o"))
e=(n2.count("u"))
f=(n2.count("A"))
g=(n2.count("E"))
h=(n2.count("I"))
i=(n2.count("O"))
j=(n2.count("U"))
print("There is a total of ",a+b+c+d+e+f+g+h+i+j,"vowels in a string")

#19. Count occurrences of each character (frequency dict).
from collections import Counter
s=input("Enter a value: ")
co=Counter(s)
print(dict(co))

#20. Capitalize the first letter of every word.
cap=input("Enter the words: ")
a=cap.capitalize()
print(a)
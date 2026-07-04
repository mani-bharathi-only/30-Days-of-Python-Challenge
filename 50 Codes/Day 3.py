'''3. Loops
11. Print the multiplication table of a number.
12. Sum of first N natural numbers.
13. Print the Fibonacci series up to N terms.
14. Check if a number is prime.
15. Print all prime numbers up to N.'''

#11 Print the multiplication table of a number.
num=int(input("Number: "))
for i in range(1,11):
    print(num*i)
#11 Square of a number
num1=int(input("Square Number: "))
for i in range(1,11):
    print(num1**i)

#12 Sum of first N natural numbers.
count=[]
for i in range(1,11):
    count.append(i)
print(count)

#13. Print the Fibonacci series up to N terms.
val=10
a,b=0,1
for _ in range(val):
    print(a,end=" ")
    a,b=b,a+b
print("\n")

#14. Check if a number is prime.
from sympy import isprime
n = 11
print(isprime(n))

#15. Print all prime numbers up to N.
N=int(input("Enter a Number: "))
for i in range(1,N+1):
    if(isprime(i)):
        print(i,end=" ")

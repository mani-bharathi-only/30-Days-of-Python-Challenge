'''2. Conditionals
Check if a number is even or odd.
Find the largest of three numbers.
Check if a year is a leap year.
Simple calculator (add/sub/mul/div based on user choice).
Grade calculator (marks → A/B/C/F).'''

#6 Check if a number is even or odd.
num=int(input("Enter a Number for odd or even: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")

#7 Find the largest of three numbers.
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(f"Largest number is {largest}")


#8 Check if a year is a leap year.
leap=int(input("Enter a number: "))
if(leap%4==0):
    print(f"{leap} is a Leap Year")
else:
    print(f"{leap} is not a Leap Year")

#9 Simple calculator (add/sub/mul/div based on user choice).
num1=int(input('Enter a num1: '))
num2=int(input("Enter a num2: "))
sum=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print(f"The Sum is {sum}")
print(f"The Sub is {sub}")
print(f"The Mul is {mul}")
print(f"The Div is {div}")

#10 Grade calculator (marks → A/B/C/F).
Tamil=int(input("Tamil: "))
English=int(input("English: "))
Maths=int(input("Maths: "))
Science=int(input("Science: "))
Total=Tamil+English+Maths+Science
Avg=Total/4
print(f"The Average is {Avg}")
if(Avg>=90):
    print("O")
elif(Avg>=80):
    print("A")
elif(Avg>=70):
    print("B")
elif(Avg>=50):
    print("C")
else:
    print("F")

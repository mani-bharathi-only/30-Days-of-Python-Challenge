#Declare your age as integer variable
age=23
print(age)

#Declare your height as a float variable
height=1.75
print(height)


complex_num=2+3j
print(complex_num)

base=float(input("enter the base of the triangle: "))
height=float(input("enter the height of the triangle: "))
area=0.5*base*height
print("Area of the triangle is:",area)

side_a=float(input("enter the side a of the triangle: "))
side_b=float(input("enter the side b of the triangle: "))
side_c=float(input("enter the side c of the triangle: "))
total=side_a+side_b+side_c
print("Sides of the triangle is:",total)

word1=len("python")
word2=len("dragon")
if(word1==word2):
    print("equal")
elif(word1>word2):
    print("python is longer than dragon")
elif(word2>word1):
    print("dragon is longer than python")
else:
    print("error")

word3="python"
float1=float(len(word3))
print(float1)
string1=str(float1)
print(string1)

#Even  or Not
num1=5
if(num1%2==0):
    print("True")
else:
    print("False")

check='10'
check2=10
print(check==check2)

#Write a script that prompts the user to enter number of years. 
#Calculate the number of seconds a person can live. Assume a person can live hundred years

Years = int(input("Enter the Number of Years: "))
Total_Years = 100
Days = 365
Hours = 24
Minutes = 60
Seconds = 60
Total_Years_Lived = Total_Years * Days * Hours * Minutes * Seconds
print(f"You have lived {Total_Years_Lived:.4E} Second")

#Write a Python script that displays the following table
print("1\t1\t1\t1\t1")
print("2\t1\t2\t4\t8")
print("3\t1\t3\t9\t27")
print("4\t1\t4\t16\t64")
print("5\t1\t5\t25\t125")

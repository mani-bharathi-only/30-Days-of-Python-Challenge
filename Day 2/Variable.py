'''
#Casting : Converting Data Types

#int to float
num_int=10
print(float(num_int))

#int to string
num_int = 29
print(str(num_int))

print() '''

#Day-2 30-Days of Python

first_name='Mani'
last_name='Bharathi'
age=20
country='India'
status='Single'
fav_color,city,fav_car=['Violet','Tirunelveli','Mercedes']
#Print the variables
print("First Name:",first_name)
print("Last Name:",last_name)
print("Age:",age)
print("Country:",country)
print("Status:",status)
print("Favorite Color:",fav_color)
print("City:",city)
print("Favorite Car:",fav_car,"\n")

#Excercise Level-2
#1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(country))
print(type(status))
print(type(fav_color))
print(type(city))
print(type(fav_car),"\n")

#2 Using the len() built-in function, find the length of your first name
print("First Name:",len(first_name),"\n")

#3 Compare the length of your first name and the length of the last name
a=(len(first_name)-len(last_name))
print(f"The Difference between the firstname and last name is {a}\n")

#4 Declare 5 as num_one and 4 as num_two
x=5
y=4
print(f"Before Swap of x={x},y={y}")
x,y=y,x
print(f"After Swap of x={x},y={y}","\n")

print(help('list'))

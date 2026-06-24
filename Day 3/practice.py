print("first")
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

print("second")
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Asabeneh'))


#Odd or Even
def is_even(num):
    if(num%2==0):
        return "The value is true"
    return"Outuput is Odd Number"
print(is_even(3))

#Even print with loop
def is_evenn(num1):
    even=[]
    for i in range(num1+1):
        if i%2==0:
            even.append(i)
    return even
print(is_evenn(40))

#Parameters
def values(first="mani",seond="bharathi"):
    fullname=first+seond
    return fullname
print(values())

#Artibritary
def sum_of_numbers(*number):
    total=0
    for num in number:
        total+=num
    return total
print("Total add",sum_of_numbers(3,2,1,5,3))

def greet(name,location):
    print("Ok",name,"where are you staying in?",location)
data={"name":"mani","location":"Madurai"}
greet(**data)
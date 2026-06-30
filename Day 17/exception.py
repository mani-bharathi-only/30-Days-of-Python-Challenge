#Exception Handling
try:
    name=input("Enter your name: ")
    age=int(input("Enter your age :"))
    print(f"Your Name{name}.Your age{age}")
except Exception as e:
    print(e)
else:
    print("An Error Occured")


def numbers(a,b,c,d):
    return a+b+c+d

lst=[1,2,3,4]
print(numbers(*lst))


def sum_all(*args):
    s=0
    for i in args:
        s+=i
    return s
print(sum_all(1,2))

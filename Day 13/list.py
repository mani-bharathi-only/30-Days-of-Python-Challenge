list1='Python'
print(list(list1))

numbers=[i for i in range(11)]
print(numbers)

#Even Numbers
numb=[i for i in range(10) if i%2==0]
print(numb)

#Lambda Function
sum_num=lambda a,b:a+b
print(sum_num(2,3))

#Self Invoking Lambda
print((lambda x,y,z:x**y+z)(2,3,4))

#Lambda inside another function
def num(x):
    return lambda y:x**y
new=num(3)
print(new(2))
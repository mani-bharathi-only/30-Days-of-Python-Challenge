'''5. Lists
21. Find the maximum and minimum in a list without built-ins.
22. Remove duplicates from a list.
23. Find the sum and average of a list.
24. Reverse a list in place.
25. Find the second largest element.'''

#21. Find the maximum and minimum in a list without built-ins
from os import dup
list1=[1,2,3,4,5,67,8,4]
max=list1[0]
min=list1[0]
for i in list1:
    if max<i:
        max=i
    if min>i:
        min=i
print("Maximum:",max)
print("Minimum:",min)

#22. Remove duplicates from a list.
a=[4,3,21,5,4,6,7,3,9]
print(list(set(a)))

#23. Find the sum and average of a list.
val=[3,3,1,5,4,7,9,6,1]
sum=0
for i in val:
    sum+=i
print("Sum:",sum)
print("Average:",sum/len(val))

#24. Reverse a list in place.
list3=[5,4,3,1,7,5,4,8,3]
list3.reverse()
print("Reversed List:",list3)

#25. Find the second largest element.
list4=[5,4,3,1,7,5,4,8,3]
list4.sort()
print("Second Largest Element:",list4[-2])


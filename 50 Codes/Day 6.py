'''6. Tuples & Sets
26. Convert a list to a tuple and access elements.
27. Find the intersection and union of two sets.
28. Check membership in a set vs a list (and why sets are faster).
29. Count unique elements in a list using a set.
30. Merge two dictionaries into one.'''

#26. Convert a list to a tuple and access elements.
list1=[1,2,3,4,5,6,7,8,9,10]
tuple1=tuple(list1)
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])
print(tuple1[6])
print(tuple1[7])
print(tuple1[8])
print(tuple1[9])

#27. Find the intersection and union of two sets.
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Intersection:",set1.intersection(set2))
print("Union:",set1.union(set2))

#28. Check membership in a set vs a list (and why sets are faster).
list2=[1,2,3,4,5]
set3={1,2,3,4,5}
print("Membership in list:",1 in list2)
print("Membership in set:",1 in set3)

#29. Count unique elements in a list using a set.
list4=[1,2,3,4,5,1,2,3,4,5]
print("Unique elements:",len(set(list4)))

#30. Merge two dictionaries into one.
dict1={1:"a",2:"b",3:"c"}
dict2={1:"d",5:"e",6:"f"}
print("Merged dictionary:",dict1.update(dict2))
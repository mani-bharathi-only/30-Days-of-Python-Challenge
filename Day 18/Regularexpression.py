import re
text="Hello bro"
match=re.search("Hello",text)
print(match)

span=match.span()
print(span)

start,end=span
print(start,end)

substring=text[start:end]
print(substring)


#File handling
f=open("file.txt","r")
k=f.read()
print(k)
f.close()

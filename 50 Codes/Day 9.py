'''9. File Handling
41. Write and read a text file.
42. Count the number of lines/words in a file.
43. Append data to an existing file.
44. Read a CSV file using the csv module.
45. Handle a file-not-found error using try/except.'''

#41. Write and read a text file.
with open("file.txt","w") as f:
    f.write("Hello World")
with open("file.txt","r") as f:
    print(f.read())

#42. Count the number of lines/words in a file.
with open("file.txt","r") as f:
    print(f.read().count("\n"))

#43. Append data to an existing file.
with open("file.txt","a") as f:
    f.write("Hello World")

#44. Read a CSV file using the csv module.
import csv
with open("file.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)


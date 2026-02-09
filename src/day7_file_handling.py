#writing in a file
file1=open("sample.txt","w")
file1.write("my name is khalid hussaini")
file1.close()

#appending a file
file2=open("sample.txt","a")
file2.write(" and iam umar farooq")
file2.close()

#reading the content of a file
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()
#topic 2
with open("sample.txt","r") as file:
    content=file.read()
    print(content)
    
#topic 3
import csv
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#topic 4
try:
    with open("sample.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error ,please check the filename")
    
#topic 5
with open("sample.txt","w+") as file:
    file.write("iam umar")
    file.seek(0,0)
    content=file.read()
    print(content)
    
    
#task1
name=input("enter your name:")
goal=input("enteryour daily goal:")

with open("journal.txt","a") as file:
    file.write(f"{name}-{goal}\n")

with open("journal.txt","r")as file:
    a=file.read()
    print(a)

#task 2
import csv

with open("student.csv","r")as file:
    reader=csv.DictReader(file)
    
    print("students who has passed:")
    for row in reader:
        if row ["Status"]=="Pass":
            print(row["Name"])
    
#task 3

filename=input("enter a filename:")
try:
    with open(filename,"r")as file:
        print(file.read())
except FileNotFoundError:
    print("OOP's that file doesn't exist yet.")
    
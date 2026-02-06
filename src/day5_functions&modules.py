#defining functions


def greet():
    print("welcome to comed kares")
   
greet()

def display_line():
    print("--------")
    
display_line()

def add(a,b):
    print(a+b)
    
result=add(2, 5)#passing parameters
print(result)#empty

x=10#global

def show_value():
    x=5#local
    print(x)
show_value()

print(x)

#chnaging global
x=5
def show():
    global x
    x=20
show()
print(x)

x=0
def addi():
   global x
   x+=1
addi()
print(x)


import math
import random

print(math.sqrt(5))
print(random.randint(10, 100))

#task 1
def calc_rectangle(length,width):#defining function
    area=length*width#calculating area
    perimeter=2*(length+width)#calculating perimeter
    return area,perimeter
calc_rectangle(3, 4)#calling the function
#input of length and width
length=int(input("enter the length:"))
width=int(input("enter the width:"))

area,perimeter=calc_rectangle(length, width)
print(f"The area of rectangle is {area}")
print(f"The perimeter of rectangle is {perimeter}")

#task 2
import math_operations

#calculating power
result_power=math_operations.power(2, 10)
print(("power is ",result_power))

numbers = [10, 20, 30, 40]
result_average = math_operations.average(numbers)
print("Average =", result_average)




#list
fruits=['orange','apple','banana','kiwi','grapes','apple']#list
print(fruits)
fruits[1]='cow'#replacing he value
print(fruits)

#tuple
fruits1=('orange','apple','banana','kiwi','grapes','apple')#tuple
print(fruits1)
fruits1[1]='cow'#erroe because tuples are immutable


fruits.reverse()
print(fruits)

fruits.remove('kiwi')#remove deletes from taking value or item
fruits.pop(1)#pop deletes from indexing number

cars=['bmw','audi','mercedes','toyata']
cars.append('rolls royce')#adding value
print(cars)
print(cars[3])
cars.count('bmw')
cars.sort()#sorting in order
print(cars)
cars.pop()#popping from last value
cars.pop(1)#popping from index number
print(cars)


#indexing and slicing
squares=[1,4,9,12,10]
print(squares)

squares[0]#indexing return the item
squares[-1]

squares[2:]#slicing returns a new list
squares[-2]

squares[2]=6 #replacing the value
squares[:]
len(squares)
squares[2:5]

#task 1

#task1
#Create a list named inventory 

inventory_list=["Apples", "Bananas", "Carrots", "Dates"]
print(inventory_list)

#Append(Eggs)

inventory_list.append("Eggs")
print(inventory_list)

#Remove(Bananas bcoz it sold out)

inventory_list.remove("Bananas")
print(inventory_list)

#organize the inventory alpabets using Sort

inventory_list.sort()
print("final updated inventory:",inventory_list)


#task2
#Create a list named temperatures
Temperature=[22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
Temperature[0]
Temperature[-1]

Afternoon_peak=Temperature[3:6]
print(Afternoon_peak)
last_3_hours=Temperature[-3:]
print(last_3_hours)

print(Temperature)
print(Temperature[0],Temperature[-1])
print(Afternoon_peak)
print(last_3_hours)

#task3
screen_res=(1920, 1080)
print("Current Resolution: 1920x1080")
print(screen_res)
screen_res[0]=1280
print("Tuples cannot be modified")

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


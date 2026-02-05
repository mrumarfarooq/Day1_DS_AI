student_name={"name":"amit","age":20,"course":"cse"}
print(student_name)

print(student_name['name'])#accessing by key
print(student_name['amit'])#error because we are accessing by value

#task 1
contacts={'umar':9880,'asif':9099,'aman':7890}
print(contacts)

contacts['afnan']=4567#adding new contact
print(contacts)
contacts['umar']=1923
print(contacts)

contacts.get('umar')
#contacts.get('maaz')
#print('contact not found')
print(contacts.get('mmaz','contact not found'))

for name, phone in contacts.items():
    print(name,phone)
    
#for key, value in contacts.items():
   # print(f"contact:{key}| Phone:{value}")


#task 2

raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]#created a list
unique_users=set(raw_logs)#converting list into set and storing in new variable

print("ID05" in unique_users)

len(raw_logs)
len(unique_users)
#1
print(len(raw_logs)^len(unique_users))
#2
print(f"{len(raw_logs)^len(unique_users)}duplicates were removed")
#3
print(f"{unique_users} and {(len(raw_logs)^len(unique_users))} dublicates were removed" )


#task 3

friend_a={'python','cooking','hiking','movies'}
friend_b={'hiking','gaming','photography','python'}

print(friend_a & friend_b)#shared interest
print(friend_a | friend_b)#all interests
print(friend_a - friend_b)#individual interest
print(friend_b - friend_a)

a=(friend_a & friend_b)
b=(friend_a | friend_b)
c=(friend_a - friend_b)

print(f"shared interest between friend a and b are {a} and all interests are {b} and individual interest of friend a are {c}")


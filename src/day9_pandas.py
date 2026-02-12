#topic 1
import pandas as pd
s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

marks=pd.Series([80,75,90],index=['maths','science','english'])
marks
print(marks['maths'])
print(marks[['maths','science']])

#topic 3
scores=pd.Series([45,60,70,80,90])
passed=scores[scores>70]
print(passed)
passed1=scores[scores<70]
passed1

#topic 4
data=pd.Series([10,None,20,None])
print(data.isnull())
print(data.fillna(30))

#topic 5
names=pd.Series(['Alice','bob','CHARLIE'],dtype="string")
print(names)
print(names[1])
print(names.str.lower())
print(names.str.contains('A'))

#task 1

import pandas as pd

products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(products['Laptop'])

print("\nFirst two products:")
print(products[:2])

#task 2
name = pd.Series( [' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
data = pd.Series([ 85, None, 92, 45, None, 78, 55]) 
print(data.isnull()) # Identify missing values
print(data.fillna(0)) # Fill missing values with 0

passed = data[data>60] # Boolean masking: scores greater than 60
print(passed)

#task3 
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()
print(cleaned)

# Check which names contain letter 'a'
contains_a = cleaned.str.contains('a')
print(contains_a)
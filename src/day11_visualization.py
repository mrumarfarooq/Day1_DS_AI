#topic 1
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,6]
plt.plot(x,y)
plt.axis((0,6,0,8))#axis giving
plt.show()

#topic 2
x1=[1,2,3,4,5]
y1=[2,3,6,8,6]
plt.scatter(x1, y1)
plt.show()

#topic 3
categories=['Laptops','Mobile','TVs','Fridge','AC']
sales=[15,30,20,5,10]
plt.bar(categories,sales)
plt.show()


#topic 4
plt.subplot(1,2,1)#row,column,position
plt.plot([1,2,3],[1,4,9])
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.plot(['A','B','C'],[3,7,5])
plt.title("Bar Chart")
plt.show()


#task 1
months=[1,2,3,4,5]
revenue=[2000,4500,4000,7500,9000]
plt.plot(months,revenue)
plt.title("Monthly Revenue Growth")
plt.xlabel("months")
plt.ylabel("revenue in us dollar")
plt.show()

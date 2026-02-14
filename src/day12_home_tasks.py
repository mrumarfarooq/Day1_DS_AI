#task 1
import matplotlib.pyplot as plt
study_hours=[1,2,3,4,5,6,7,8]
scores=[50,55,65,70,75,85,90,95]
plt.scatter(study_hours,scores)
plt.show()

#task 2
plt.subplot(1,2,1)
plt.bar(['Electronics','Clothing','Home'],[300,450,200])
plt.title("Bar Chart")

plt.subplot(1,2,2)
plt.plot([1,2,3],[5,7,10])
plt.title("Line Plot")
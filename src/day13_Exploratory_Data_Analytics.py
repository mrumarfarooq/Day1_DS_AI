#topic 1
import pandas as pd
df=pd.read_csv("Employee_Salary.csv")

df.head()
df.tail()
df.shape
df.info()
df.describe()


#topic 2
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Age'],kde=True)
plt.show()

sns.boxplot(x=df['Salary'])
plt.show()

df['Performance'].value_counts()

#topic 3
sns.scatterplot(x='Age',y='Salary', data=df)
plt.show()

sns.boxplot(x='Performance',y='Salary',data=df)
plt.show()

#task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel("Housing_with_City.xlsx")
plt.subplot(1,2,1)
sns.histplot(df['price'],kde=True)

#calculating skewness and kurtosis
print("skewness of price column:",df['price'].skew())
print("kurtosis of price column:",df['price'].kurt())

#countplot
plt.subplot(1,2,2)
sns.countplot(x="City", data=df)
plt.title("City frequency")
plt.show()


#task 2

df=pd.read_excel("Housing_with_City.xlsx")

plt.subplot(1,2,1)
plt.scatter(df['area'],df['price'])
plt.title("House Area vs Price")
plt.show()

plt.subplot(1,2,2)
sns.boxplot(x='City',y='price',data=df)
plt.title("Price distribution by city")
plt.xlabel("City")

plt.ylabel("Price")
plt.show()

#task 3

df=pd.read_excel("Housing_with_City.xlsx")

corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
plt.subplot(1,2,1)
sns.heatmap(corr_matrix,annot=True)
plt.show()

plt.subplot(1,2,2)
sns.boxplot(x=df['price'])
plt.show()
plt.tight_layout()

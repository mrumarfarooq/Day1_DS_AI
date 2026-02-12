import pandas as pd

data={
      
      "CustomerID":[101,102,101,104,105],
      "Name":["Umar","Farooq",None,"Asif","Maaz"],
      "Age":[20,21,23,None,50],
      "City":["Bijapur",None,"   Delhi","PUNE","Delhi"],
      "Payment":["UPI",None,"Card","Cash","UPI"]
      
      }

df=pd.DataFrame(data)

df.head()#shows first 5 rows
df.head(2)#shows specific rows
df.info()

#checking missing values
print("missing values per column")
print(df.isna().sum())

#filling missing values(stastical approach)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Name"]=df["Name"].fillna("Unknown")
df["City"]=df["City"].fillna(df["City"].mode()[0])#most occured name
df["Payment"]=df["Payment"].fillna(df["Payment"].mode()[0])

#check data types 
print(df.dtypes)

#converting data types
df["Age"]=df["Age"].astype(int)
print(df.dtypes)

#string cleaning
df["City"]=df["City"].str.strip()#removing spaces
df["City"]=df["City"].str.lower()
print(df["City"])

#duplicate handling
print(df)
print(df.duplicated().sum())#duplicates are not on this dataset
df=df.drop_duplicates()
df.shape

#task 1
import csv
import numpy as np
data1=pd.read_csv("customer_order.csv")
df1=pd.DataFrame(data1)
print("shape before cleaning",df1.shape)
#report missing values
print(df1.isna().sum())
#filling missing values

numeric_cols = df1.select_dtypes(include=[np.number]).columns

df1[numeric_cols] = df1[numeric_cols].fillna(df1[numeric_cols].median())

df1=df1.drop_duplicates()
print("Shape after cleaning",df1.shape)
print(df1)

#task 2
import pandas as pd
data2={
       "Date":["2026-01-01","2026-01-02","2026-01-03","2026-01-04"],
       "Price":["$100.50","$200.75","$300.20","$400.10"]
       }
df2=pd.DataFrame(data2)
print(df2)
#data types
print(df2.dtypes)
#converting data types
df2["Price"]=df2["Price"].str.replace("$","",regex=False).astype(float)#removing dollar
print(df2)
print(df2.dtypes)#changed datatype

df2["Date"]=pd.to_datetime(df2["Date"])
print(df2)
print(df2.dtypes)

#task 3
import pandas as pd
data3={
       "Location":[" New York","new york","NEW YORK ","New York"]
       }
df3=pd.DataFrame(data3)
print(df3)
#before cleaning
df3.groupby("Location").size()
print(df3["Location"].unique())
#cleaning
df3["Location"]=df3["Location"].str.strip()
df3["Location"]=df3["Location"].str.title()#or you can use str.lower
#after cleaning
print(df3["Location"].unique())
df3.groupby("Location").size()

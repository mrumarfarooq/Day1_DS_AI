#task 1
import pandas as pd

#sample dataset
df=pd.read_csv("Car_datasets.csv")
df

#label encoding
df["Transmission"]=df["Transmission"].map({"Automatic":1,"Manual":0})
df

#one hot encoding
df_encoded=pd.get_dummies(df,columns=['Color'],drop_first=True)
df_encoded

#task 2
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler

df1=pd.read_csv("Employee_Salary.csv")
df1

#select numeric features
features=df1[["Age","Salary"]]

#standardization
std_scaler=StandardScaler()
standardized=std_scaler.fit_transform(features)
df_std=pd.DataFrame(standardized,columns=["Age_std","Salary_std"])
df_std

#normalization
mmscaler=MinMaxScaler()
normalized=mmscaler.fit_transform(features)
df_norm=pd.DataFrame(normalized,columns=["Age_norm","Salary_norm"])
df_norm

#histogram
plt.figure(figsize=(12,4))

#original salary plot
plt.subplot(1,3,1)
plt.hist(df1['Salary'])
plt.title("Original Salary")

#standardized salary
plt.subplot(1,3,2)
plt.hist(df_std['Salary_std'])
plt.title("Standardized Salary")

#Normalized salary
plt.subplot(1,3,3)
plt.hist(df_norm['Salary_norm'])
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()



#task3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load dataset
df2 = pd.read_csv("Employee_Salary.csv")

# Feature & Target
X = df2[["Experience"]]   # Non-linear feature
y = df2["Salary"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Simple Linear Model

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_lin)

# 2. Polynomial Model

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_pred_poly = poly_model.predict(X_poly_test)
r2_poly = r2_score(y_test, y_pred_poly)

# Output

print("R2 Score (Linear):", r2_linear)
print("R2 Score (Polynomial):", r2_poly)

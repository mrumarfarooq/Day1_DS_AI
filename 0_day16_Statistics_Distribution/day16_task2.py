#task 2
import numpy as np
import pandas as pd

np.random.seed(0)

data = pd.DataFrame({
    "values": np.random.normal(50, 10, 100)
})

data.loc[100] = 120
data.loc[101] = -10

mean = data["values"].mean()
std = data["values"].std()

data["z_score"] = (data["values"] - mean) / std

outliers = data[abs(data["z_score"]) > 3]

print("Mean (μ):", round(mean,2))
print("Standard Deviation (σ):", round(std,2))
print("\nOutliers (|Z| > 3):")
print(outliers)



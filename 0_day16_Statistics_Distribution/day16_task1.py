import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random numerical data
np.random.seed(42)

#Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Income)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Test Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Create DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
#normal distribtion
plt.figure(figsize=(8,5))
sns.histplot(df["Heights"], kde=True)
plt.title("Normal Distribution - Heights")
plt.show()


#Right skew distribtion

plt.figure(figsize=(8,5))
sns.histplot(df["Incomes"], kde=True)
plt.title("Right-Skewed Distribution - Income")
plt.show()

#left skew distribtion

plt.figure(figsize=(8,5))
sns.histplot(df["Scores"], kde=True)
plt.title("Left-Skewed Distribution - Easy Exam Scores")
plt.show()


print("Heights → Mean:", df["Heights"].mean(),
      "Median:", df["Heights"].median())

print("Incomes → Mean:", df["Incomes"].mean(),
      "Median:", df["Incomes"].median())

print("Scores → Mean:", df["Scores"].mean(),
      "Median:", df["Scores"].median())
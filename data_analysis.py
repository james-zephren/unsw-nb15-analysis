import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("UNSW_NB15_training-set.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check basic info
print("\nDataset Info:")
print(df.info())

# Basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop duplicates and missing data
df = df.drop_duplicates().dropna()

# Confirm shape after cleaning
print("\nShape after cleaning:", df.shape)

# Example: Count of attack categories
plt.figure(figsize=(10,5))
sns.countplot(x='attack_cat', data=df, order=df['attack_cat'].value_counts().index)
plt.title("Distribution of Attack Categories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

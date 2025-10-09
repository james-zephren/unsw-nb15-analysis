import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("UNSW_NB15_training-set.csv")

# Preview the dataset
print("🔹 First 5 rows:")
print(df.head())

# Check dataset shape
print("\n🔹 Rows and columns:", df.shape)

# Column names
print("\n🔹 Column names:", df.columns.tolist())

# Data types
print("\n🔹 Data types:")
print(df.dtypes)

# Summary statistics
print("\n🔹 Summary statistics:")
print(df.describe())

# Missing values
print("\n🔹 Missing values per column:")
print(df.isnull().sum())

# --- Simple Visualization ---
# Replace 'ColumnName' with one of your numeric column names
df['ColumnName'].hist(bins=20, edgecolor="black")
plt.title("Distribution of ColumnName")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

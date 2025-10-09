import matplotlib.pyplot as plt
import seaborn as sns

# Example: Count of attack categories
plt.figure(figsize=(10,5))
sns.countplot(x='attack_cat', data=df, order=df['attack_cat'].value_counts().index)
plt.title("Distribution of Attack Categories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

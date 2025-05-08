#Task 3 Data Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')

print(df.head())

sns.pairplot(df, hue='species', corner=True)
plt.suptitle("Pairwise Relationships in Iris Dataset", y=1.02)
plt.show()

for col in df.columns[:-1]:  
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.show()

for col in df.columns[:-1]:
    sns.boxplot(x='species', y=col, data=df)
    plt.title(f'{col} by Species')
    plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df.drop('species', axis=1).corr(), annot=True, cmap='Blues')
plt.title("Feature Correlation in Iris Dataset")
plt.show()

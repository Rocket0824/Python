#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate the dataset based on the provided description
np.random.seed(42)
data = {
    'CRIM': np.random.exponential(scale=1.0, size=506),
    'ZN': np.random.uniform(0, 100, size=506),
    'INDUS': np.random.uniform(0, 30, size=506),
    'CHAS': np.random.choice([0, 1], size=506),
    'NOX': np.random.uniform(0.3, 0.9, size=506),
    'RM': np.random.uniform(3, 9, size=506),
    'AGE': np.random.uniform(0, 100, size=506),
    'DIS': np.random.uniform(1, 12, size=506),
    'RAD': np.random.randint(1, 25, size=506),
    'TAX': np.random.uniform(180, 720, size=506),
    'PTRATIO': np.random.uniform(12, 22, size=506),
    'LSTAT': np.random.uniform(2, 38, size=506),
    'MEDV': np.random.uniform(5, 50, size=506)
}

df = pd.DataFrame(data)

# Discretize AGE into three groups: <=35, 36-70, >70
df['AGE_group'] = pd.cut(df['AGE'], bins=[0, 35, 70, 100], labels=['<=35', '36-70', '>70'])

# Plot 1: Boxplot for MEDV
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['MEDV'])
plt.title('Boxplot of Median Value of Owner-Occupied Homes (MEDV)')
plt.ylabel('MEDV ($1000s)')
plt.show()

# Plot 2: Bar plot for CHAS
plt.figure(figsize=(8, 6))
sns.countplot(x=df['CHAS'])
plt.title('Bar Plot for Charles River Variable (CHAS)')
plt.xlabel('CHAS (0 = Does not bound, 1 = Bounds)')
plt.ylabel('Count')
plt.show()

# Plot 3: Boxplot of MEDV vs AGE_group
plt.figure(figsize=(8, 6))
sns.boxplot(x='AGE_group', y='MEDV', data=df)
plt.title('Boxplot of MEDV by AGE Group')
plt.xlabel('Age Group')
plt.ylabel('MEDV ($1000s)')
plt.show()

# Plot 4: Scatter plot of NOX vs INDUS
plt.figure(figsize=(8, 6))
sns.scatterplot(x='INDUS', y='NOX', data=df)
plt.title('Scatter Plot of NOX vs INDUS')
plt.xlabel('Proportion of Non-Retail Business Acres (INDUS)')
plt.ylabel('Nitric Oxides Concentration (NOX)')
plt.show()

# Plot 5: Histogram for PTRATIO
plt.figure(figsize=(8, 6))
sns.histplot(df['PTRATIO'], kde=True, bins=20)
plt.title('Histogram of Pupil-Teacher Ratio (PTRATIO)')
plt.xlabel('Pupil-Teacher Ratio')
plt.ylabel('Frequency')
plt.show()


# In[ ]:





'''Constructing contingency tables (also called cross-tabulations) in Python is a common task in data analysis, especially when working with categorical data. A contingency table summarizes the relationship between two or more categorical variables.'''

#Example 1: Constructing a Simple Contingency Table
'''Dataset

Gender	Purchased
Male	Yes
Female	No
Male	No
Female	Yes
Male	Yes
Female	Yes'''

import pandas as pd

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Construct the contingency table
contingency_table = pd.crosstab(df['Gender'], df['Purchased'])

# Display the contingency table
print(contingency_table)

'''output:
    
Purchased  No  Yes
Gender          
Female     1    2
Male       1    2'''

#Example 2: Contingency Table with Multiple Variables
'''If you have more than two categorical variables, you can still use pd.crosstab() to create a contingency table. For example, let's say we add an additional variable for Age Group.

Dataset:

Gender	Purchased	Age Group
Male	Yes	18-25
Female	No	26-35
Male	No	18-25
Female	Yes	26-35
Male	Yes	36-45
Female	Yes	18-25'''

# Sample data with an additional variable "Age Group"
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes'],
    'Age Group': ['18-25', '26-35', '18-25', '26-35', '36-45', '18-25']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Construct the contingency table with 3 variables
contingency_table = pd.crosstab([df['Gender'], df['Age Group']], df['Purchased'])

# Display the contingency table
print(contingency_table)

'''output:
    Purchased                No  Yes
Gender Age Group               
Female 18-25             0    1
       26-35             1    1
Male   18-25             1    0
       36-45             0    1'''

#Example 3: Normalized Contingency Table
'You can normalize the contingency table to show proportions or percentages instead of raw counts. This can be useful for understanding the relative frequency of each category.

# Construct the contingency table and normalize by the total number of observations
normalized_table = pd.crosstab(df['Gender'], df['Purchased'], normalize='all')

# Display the normalized contingency table
print(normalized_table)

'''output:
Purchased       No  Yes
Gender                
Female    0.166667  0.333333
Male      0.166667  0.333333'''

#Example 4: Statistical Test on Contingency Table (Chi-Square Test)
'''Once you have a contingency table, you can use it to perform statistical tests, like the Chi-square test of independence, to determine if there is a significant relationship between the two categorical variables.

To perform a Chi-square test, you can use scipy.stats.chi2_contingency().'''

from scipy.stats import chi2_contingency

# Construct a contingency table
contingency_table = pd.crosstab(df['Gender'], df['Purchased'])

# Perform the Chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Display the results
print(f"Chi-square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Counts:")
print(expected)

'''output:
Chi-square Statistic: 0.0
P-value: 1.0
Degrees of Freedom: 1
Expected Counts:
[[1. 2.]
 [1. 2.]]'''

#Example 5: Creating a Contingency Table from Multiple Columns in a DataFrame
'If you want to construct a contingency table from multiple columns in a DataFrame, you can use pd.crosstab() with normalize='columns' or normalize='index' to see relative frequencies per category.

# Example dataset with multiple categorical columns
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes'],
    'Region': ['North', 'South', 'East', 'West', 'East', 'West']
}

df = pd.DataFrame(data)

# Construct the contingency table with normalization by 'Region'
contingency_table = pd.crosstab(df['Gender'], df['Region'], normalize='columns')

# Display the normalized contingency table
print(contingency_table)

'''output:
Region   East  North  South  West
Gender                          
Female   0.5   0.0    0.5   0.5
Male     0.5   1.0    0.5   0.5'''




"""
Program: Correlation Analysis between Two Nominal Attributes
Purpose: Calculate and interpret correlation using:
1. Chi-squared test
2. Cramer's V statistic

-----------------------Algorithm-------------------------------------------------
Read CSV file containing two nominal columns (e.g., Gender and Preference)
Store data in a pandas DataFrame
Create Contingency Table

Use pd.crosstab() to create a contingency table
Rows represent one nominal attribute (e.g., Gender)
Columns represent the other nominal attribute (e.g., Preference)
Perform Chi-squared Test

Use chi2_contingency() from scipy.stats to perform the Chi-squared test on the contingency table
Extract the Chi-squared statistic (chi2)
Calculate Total Number of Observations

Sum all values in the contingency table to get the total number of observations (n)
Calculate Cramer's V Statistic

Use the formula: V = sqrt(chi2 / (n * (min(rows-1, columns-1))))
Where rows and columns are the dimensions of the contingency table
Output Results

Print the Chi-squared statistic
Print Cramer's V statistic
Interpret Cramer's V Value

If Cramer's V < 0.1: Weak association
If 0.1 <= Cramer's V < 0.3: Moderate association
If Cramer's V >= 0.3: Strong association

---------------------------------------------------------------------------------
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Read CSV file into DataFrame
df = pd.read_csv('data/Corr_Nom_Attr.csv')

# Create a contingency table
# Rows: Gender, Columns: Preference
contingency_table = pd.crosstab(df['Gender'], df['Preference'])
print("Contingency Table:")
print(contingency_table)

# Perform Chi-squared test
# chi2: Chi-squared statistic
# _: p-value (not used here)
# _: degrees of freedom (not used here)
# _: expected frequencies (not used here)
chi2, _, _, _ = chi2_contingency(contingency_table)

# Calculate total number of observations
n = contingency_table.sum().sum()

# Calculate Cramer's V statistic
# Formula: V = sqrt(chi2 / (n * (min(rows-1, columns-1))))
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape[0] - 1, contingency_table.shape[1] - 1))))

# Print Chi-squared statistic and Cramer's V
print(f'Chi2: {chi2}')
print(f'Cramer\'s V: {cramers_v}')

# Interpret Cramer's V value
# < 0.1: Weak association
# 0.1 - 0.3: Moderate association
# > 0.3: Strong association
if cramers_v < 0.1:
    print('Weak association')
elif cramers_v < 0.3:
    print('Moderate association')
else:
    print('Strong association')
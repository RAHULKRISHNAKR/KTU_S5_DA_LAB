"""
Program: Correlation Analysis between Two Numerical Attributes
Purpose: Calculate and compare correlation using:
1. Manual calculation with step-by-step implementation
2. Built-in pandas functions

-----------------------Algorithm-------------------------------------------------
Algorithm for Correlation Analysis between Two Numerical Attributes
Input

Read CSV file containing two numerical columns A and B
Store data in a pandas DataFrame
Get number of records (n)
Convert columns to lists for calculations
Calculate Means

Calculate mean of column A: col1_mean = sum(A)/n
Calculate mean of column B: col2_mean = sum(B)/n
Calculate Covariance

For each pair of values (i=1 to n):
Calculate (A[i] - mean_A) * (B[i] - mean_B)
Add to running sum
Divide sum by (n-1) to get covariance
Calculate Standard Deviations

For column A:
Sum (A[i] - mean_A)² for all i
Divide by (n-1) to get variance
Take square root for standard deviation
For column B:
Sum (B[i] - mean_B)² for all i
Divide by (n-1) to get variance
Take square root for standard deviation
Calculate Correlation Coefficient

Correlation = Covariance / (sd_A * sd_B)
Verify Results

Compare manual calculations with pandas built-in functions
Print covariance and correlation values
Interpret Results

If correlation > 0: Positive correlation
If correlation < 0: Negative correlation
If correlation = 0: No correlation
---------------------------------------------------------------------------------
"""

import pandas as pd 
import numpy as np

# Read CSV file into DataFrame
df = pd.read_csv('data/Corr_Num_Attr.csv')
n = len(df)

# Convert columns to lists for manual calculation
col1 = df['A'].tolist()
col2 = df["B"].tolist()

# Step 1: Calculate means for both columns
col1_mean = sum(col1)/n
col2_mean = sum(col2)/n

# Step 2: Calculate covariance
# Formula: Covariance = Σ((x-x̄)(y-ȳ))/(n-1)
summation = 0
for i in range(n):
    summation += (col1[i]-col1_mean)*(col2[i]-col2_mean)
cov = summation/(n-1)

# Step 3: Calculate variance and standard deviation for X
# Formula: σ² = Σ(x-x̄)²/(n-1)
var_x = 0
for i in range(n):
    var_x += (col1[i]-col1_mean)**2
var_x = var_x/(n-1)
sd_X = np.sqrt(var_x)

# Step 4: Calculate variance and standard deviation for Y
var_y = 0
for i in range(n):
    var_y += (col2[i]-col2_mean)**2
var_y = var_y/(n-1) 
sd_Y = np.sqrt(var_y)

# Step 5: Calculate correlation coefficient
# Formula: ρ = covariance/(sd_X * sd_Y)
corr = cov/(sd_X*sd_Y)

# Display manual calculation results
print("Manually Computed Values:")
print(f"\tCovariance : {cov}")
print(f"\tCorrelation : {corr}")

# Compare with pandas built-in functions
print("Using Pandas:")
print(f"\tCovariance : {df['A'].cov(df['B'])}")
print(f"\tCorrelation : {df['A'].corr(df['B'])}")

# Interpret correlation result
# Positive: variables move in same direction
# Negative: variables move in opposite directions
# Zero: no linear relationship
if corr>0:
    print("Positive Correlation")
elif corr<0:
    print("Negative Correlation")
else:
    print("No Correlation")

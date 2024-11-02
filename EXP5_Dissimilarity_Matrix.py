'''
--------------------Algorithm---------------------------------------------------
 This program calculates three types of dissimilarity matrices:
 1. Numerical - for continuous values like age, salary
 2. Nominal - for categorical values like department
 3. Mixed - combines both numerical and nominal dissimilarities


Read CSV file containing employee data with numerical and nominal attributes
Data includes: age, salary (numerical) and department (nominal)
Initialization

Get number of records (n) from input data
Create three n×n matrices filled with zeros:
num_dissmat for numerical attributes
nom_dissmat for nominal attributes
mix_dissmat for combined dissimilarity
Calculate Numerical Dissimilarity

For each pair of records (i,j):
Calculate absolute difference between numerical values
Sum these differences
Store in num_dissmat[i][j]
Calculate Nominal Dissimilarity

For each pair of records (i,j):
Count number of mismatches in categorical values
Store count in nom_dissmat[i][j]
Calculate Mixed Dissimilarity

For each pair of records (i,j):
If i >= j:
Calculate average of numerical and nominal dissimilarities
Store in mix_dissmat[i][j]
Else:
Copy symmetric value from lower triangle
Output

Display all three dissimilarity matrices
Format output without row/column labe

--------------------------------------------------------------------------------- 
'''
import pandas as pd
import numpy as np

# Read the input data
df = pd.read_csv('Data\Dissimilarity_Matrix.csv')

# Initialize matrix for numerical attributes (like age, salary)
num_dissmat = np.zeros((len(df), len(df)))

# Calculate numerical dissimilarity (Manhattan distance)
for i in range(len(df)):
    for j in range(len(df)):
        # Sum of absolute differences between rows i and j
        num_dissmat[i][j] = np.sum(np.abs(df.iloc[i] - df.iloc[j]))

# Initialize matrix for nominal/categorical attributes
nom_dissmat = np.zeros((len(df), len(df)))

# Calculate nominal dissimilarity (count of unequal attributes)
for i in range(len(df)):
    for j in range(len(df)):
        # Count number of mismatches between rows i and j
        nom_dissmat[i][j] = np.sum(df.iloc[i] != df.iloc[j])

# Initialize matrix for combined dissimilarity
mix_dissmat = np.zeros((len(df), len(df)))

# Calculate mixed dissimilarity (average of numerical and nominal)
for i in range(len(df)):
    for j in range(len(df)):
        if i >= j:
            # Average of numerical and nominal dissimilarities
            mix_dissmat[i][j] = (num_dissmat[i][j] + nom_dissmat[i][j])/2
        else:
            # Matrix is symmetric, copy from lower triangle
            mix_dissmat[i][j] = mix_dissmat[j][i]

# Print matrices without row/column labels for clarity
print("Numerical Dissimilarity Matrix:")
print(pd.DataFrame(num_dissmat).to_string(index=False, header=False))
print("\nNominal Dissimilarity Matrix:")
print(pd.DataFrame(nom_dissmat).to_string(index=False, header=False))
print("\nMixed Dissimilarity Matrix:")
print(pd.DataFrame(mix_dissmat).to_string(index=False, header=False))
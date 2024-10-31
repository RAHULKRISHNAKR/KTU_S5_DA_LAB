'''
--------------------Algorithm----------------------------------
1. Load Data:

Read the data values from your file (like a CSV) and store them in a list.
2. Sort Data:

Arrange the data values in order from smallest to largest.
3. Calculate Quartiles:

Q1 (25th percentile): The value that separates the lowest 25% of the data.
Q2 (50th percentile): The middle value (same as the median).
Q3 (75th percentile): The value that separates the lowest 75% of the data.
4. Find Outliers:

IQR (Interquartile Range): Calculate the difference between Q3 and Q1.
Upper Bound: Q3 + (1.5 * IQR)
Lower Bound: Q1 - (1.5 * IQR)
Any values above the upper bound or below the lower bound are considered outliers.
5. Remove Outliers (Optional):

Create a new list without the outlier values.
6. Calculate Mean:

Add up all the values (excluding outliers if removed).
Divide the sum by the total number of values.
7. Calculate Median:

If there's an odd number of values, the median is the middle value.
If there's an even number of values, the median is the average of the two middle values.
8. Calculate Mode:

Create a dictionary to store each value and how many times it appears.
Go through each value:
If the value is already in the dictionary, increase its count.
If not, add the value to the dictionary with a count of 1.
The value(s) with the highest count is the mode.
9. Calculate Variance:

For each value, find the difference between the value and the mean, then square that difference.
Add up all the squared differences.
Divide the sum by the total number of values minus 1.
10. Calculate Standard Deviation:

Take the square root of the variance.
11. Display Results:

Show the calculated quartiles, mean, median, mode, variance, and standard deviation.
---------------------------------------------------------------
'''

import pandas as pd

# Initialize variables for mean, median, mode, mode count, and a dictionary for mode calculation
mean,median,mode=0,0,0
d={}
out=[]
modcount=0

# Read data from the CSV file
data = pd.read_csv('Data\Statistical Description.csv')
# Extract the 'Values' column as a list
values = data['Values'].tolist()
# Sort the values in ascending order
values.sort()
# Print the sorted values
print(values)

# Calculate and print the quartiles of the data
print("Quartiles: ")
print("\tQ0: ",min(values)) # Minimum value (0th percentile)
print("\tQ1: ",values[len(values)//4]) # First quartile (25th percentile)
print("\tQ2: ",values[len(values)//2]) # Second quartile (median, 50th percentile)
print("\tQ3: ",values[3*len(values)//4]) # Third quartile (75th percentile)
print("\tQ4: ",max(values)) # Maximum value (100th percentile)
print()

# Calculate and print the interquartile range (IQR)
iqr = values[3*len(values)//4]-values[len(values)//4]
print(f"IQR: {iqr}")

# Calculate and print the upper and lower bounds for outlier detection
h0 = values[3*len(values)//4] + (1.5*iqr)
l0 = values[len(values)//4] - (1.5*iqr)
print(f"h0: {h0}")
print(f"l0: {l0}")

# Identify and print outliers below the lower bound
p=0
for i in range(0,len(values)//4):
    if values[i]<l0:
        p+=1
        out.append(values[i])
        print(values[i],end=", ")
    else: 
        if p==0:
            print('None')
        break

# Identify and print outliers above the upper bound
p=0
for i in range(len(values)-1,3*len(values)//4,-1):
    if values[i]>h0:
        p+=1
        out.append(values[i])
        print(values[i],end=", ")
    else: 
        if p==0:
            print('None')
        break

# Remove outliers from the values list
while(out):
    values.remove(out.pop())
# Print the values list after removing outliers
print(values)  

# Calculate and print the mean of the data (excluding outliers)
for val in values:
    mean += val
mean = mean/(len(values))
print(f"Mean: {mean}")

# Calculate and print the median of the data (excluding outliers)
if len(values) % 2 == 0:
    median = (values[len(values)//2]+values[len(values)//2+1])//2
else:
    median = values[len(values)//2]
print(f"Median: {median}")

# Calculate the mode of the data (excluding outliers)
for val in values:
    if val not in d.keys():
        d[val]=1
    else:
        d[val]+=1
temp=0
for key,value in d.items():
    if value>temp:
        temp=value
        mode=key

# Print the mode(s) of the data
print("Mode:" , end=" " )
for key,value in d.items():
    if value == temp:
        modcount+=1
        print(key, end=", ")
print()

# Determine and print the type of mode (unimodal, bimodal, multimodal, or no mode)
if modcount==0:
    print("No mode")
elif(modcount==1):
    print("Unimode")
elif(modcount==2):
    print("Bimode")
else:
    print("Multimode")

print()

# Calculate and print the variance and standard deviation of the data (excluding outliers)
sqsum=0
for num in values:
    sqsum += (num-mean)**2
var = sqsum/(len(values)-1)
sd = var**0.5

print(f"Variance: {var}")
print(f"Standard Deviation: {sd}")

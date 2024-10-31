'''
---------------Algorithm---------------------------
1. Get the Data:

Read the data values from a file (like a CSV) or a list.
2. Calculate the Mean (Average):

Add up all the data values.
Divide the sum by the total number of values.
3. Calculate the Median (Middle Value):

Sort the data values from smallest to largest.
If there's an odd number of values, the median is the middle value.
If there's an even number of values, the median is the average of the two middle values.
4. Calculate the Mode (Most Frequent Value):

Create a dictionary (like a table) to store each value and how many times it appears.
Go through each data value:
If the value is already in the dictionary, increase its count.
If not, add the value to the dictionary with a count of 1.
Find the value(s) with the highest count in the dictionary – that's the mode.
5. Show the Results:

Print or display the calculated mean, median, and mode.
In simpler terms:

Mean: Like finding the average score in a class.
Median: The middle value when you line up all the values.
Mode: The value that appears most often.
----------------------------------------------------------------------------------
'''

import pandas as pd

# Initialize variables to store mean, median, and mode
mean,median,mode=0,0,0
# Initialize an empty dictionary to store the frequency of each value for mode calculation
d={}

# Read data from the CSV file named 'Central_Tendencies.csv' located in the 'Data' folder
data = pd.read_csv('Data\Central_Tendencies.csv')

# Extract the values from the 'Values' column of the DataFrame and store them in a list called 'values'
values = data['Values'].tolist()

# Print the unsorted list of values
print(values)

# Sort the values in ascending order to facilitate median and mode calculation
values.sort()

# Calculate the median of the sorted values
if len(values) % 2 == 0:
    # If the number of values is even, the median is the average of the two middle values
    median = (values[len(values)//2]+values[len(values)//2+1])//2
else:
    # If the number of values is odd, the median is the middle value
    median = values[len(values)//2]

# Calculate the mean of the values
for val in values:
    mean += val
mean = mean/(len(values))

# Calculate the mode of the values
for val in values:
    # If the value is not in the dictionary, add it with a count of 1
    if val not in d.keys():
        d[val]=1
    # If the value is already in the dictionary, increment its count by 1
    else:
        d[val]+=1

# Find the maximum frequency (count) from the dictionary
temp=0
for key,value in d.items():
    if value>temp:
        temp=value
        # Store the value (key) with the maximum frequency as the mode
        mode=key

# Print the calculated central tendencies (mean, median, and mode)
print("Central Tendencies: ")
print(f"Mean: {mean}")
print(f"Median: {median}")
print("Mode:" , end=" " )
# Iterate through the dictionary and print all values (keys) that have the maximum frequency (mode)
for key,value in d.items():
    if value == temp:
        print(key, end=", ")
print()

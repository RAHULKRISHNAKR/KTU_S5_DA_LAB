'''
-----------------QUESTION------------------------------------------------------------------------
Write a program to find the dissimilarity of nominal numeric and mixed type of attributes

-----------------Algorithm-----------------------------------------------------------------------
0.Start
Input Collection:
1.1. Prompt the user to enter the number of records (num_records).

1.2. Prompt the user to enter the number of attributes (num_attributes).

1.3. For each attribute (from 1 to num_attributes):
- Ask the user to specify the type of the attribute: nominal or numeric.
- Store the attribute type in a list (attribute_types).

1.4. For each record (from 1 to num_records):
- Ask the user to input the values for all attributes of that record, separated by spaces.
- Convert numeric attributes to float.
- Store the record in a list (records).

Normalization of Numeric Attributes:
2.1. Identify numeric attributes by their indices using the attribute_types list.

2.2. Extract all numeric values from the records based on the identified indices.

2.3. Calculate the minimum and maximum values for each numeric attribute across all records.

2.4. Normalize each numeric value by transforming it to a value between 0 and 1 using the formula:

normalized value
=
original value
−
min value
max value
−
min value
normalized value= 
max value−min value
original value−min value
​
 
2.5. Replace the original numeric values in the records with their normalized values.

Dissimilarity Calculation:
3.1. For each pair of records (record i and record j, where 
𝑖
<
𝑗
i<j):

perl
Copy code
 3.1.1. Initialize a variable `dissimilarity` to 0.
 
 3.1.2. **For each attribute** (from 1 to `num_attributes`):
 
     - If the attribute is `nominal`:
         - Add `1` to `dissimilarity` if the values differ between the two records, else add `0`.
     
     - If the attribute is `numeric`:
         - Add the absolute difference between the normalized values of the two records for this attribute to `dissimilarity`.
 
 3.1.3. **Output the dissimilarity score** for the pair of records `i` and `j`.

 4.Stop
 ======================================CODE==============================================================================================
'''

import numpy as np

def nominal_dissimilarity(a, b):
    """Calculate dissimilarity between two nominal attributes."""
    return 1 if a != b else 0

def numeric_dissimilarity(a, b):
    """Calculate dissimilarity between two numeric attributes (using normalized absolute difference)."""
    return abs(a - b)

def mixed_dissimilarity(record1, record2, attribute_types):
    """Calculate dissimilarity between two records with mixed attribute types."""
    dissimilarity = 0
    for i, attr_type in enumerate(attribute_types):
        if attr_type == 'nominal':
            dissimilarity += nominal_dissimilarity(record1[i], record2[i])
        elif attr_type == 'numeric':
            dissimilarity += numeric_dissimilarity(record1[i], record2[i])
        else:
            raise ValueError(f"Unknown attribute type: {attr_type}")
    return dissimilarity

def normalize_numeric_values(records, numeric_indices):
    """Normalize numeric attributes in a dataset."""
    numeric_values = np.array([[record[i] for i in numeric_indices] for record in records])
    min_vals = numeric_values.min(axis=0)
    max_vals = numeric_values.max(axis=0)
    range_vals = max_vals - min_vals
    
    normalized_records = []
    for record in records:
        normalized_record = list(record)
        for i, index in enumerate(numeric_indices):
            normalized_record[index] = (record[index] - min_vals[i]) / range_vals[i] if range_vals[i] != 0 else 0
        normalized_records.append(normalized_record)
    
    return normalized_records

if __name__ == "__main__":
    num_records = int(input("Enter the number of records: "))
    records = []
    attribute_types = []

    print("\nEnter attribute types (nominal/numeric) for each attribute:")
    num_attributes = int(input("Enter the number of attributes: "))
    for i in range(num_attributes):
        attr_type = input(f"Attribute {i + 1} type: ")
        attribute_types.append(attr_type)
    
    print("\nEnter the records (one attribute per line, separated by spaces):")
    for i in range(num_records):
        record = input(f"Record {i + 1}: ").split()
        for j, attr_type in enumerate(attribute_types):
            if attr_type == 'numeric':
                record[j] = float(record[j])
        records.append(record)
    
    # Normalize numeric attributes
    numeric_indices = [i for i, attr_type in enumerate(attribute_types) if attr_type == 'numeric']
    normalized_records = normalize_numeric_values(records, numeric_indices)

    # Compute dissimilarity between all pairs of records
    print("\nDissimilarity between pairs of records:")
    for i in range(len(normalized_records)):
        for j in range(i + 1, len(normalized_records)):
            dissimilarity = mixed_dissimilarity(normalized_records[i], normalized_records[j], attribute_types)
            print(f"Dissimilarity between Record {i + 1} and Record {j + 1}: {dissimilarity:.4f}")

'''
----------------------------------------------EXAMPLE USAGE------------------------------------------------------------------------
Enter the number of records: 3

Enter attribute types (nominal/numeric) for each attribute:
Enter the number of attributes: 2
Attribute 1 type: nominal
Attribute 2 type: numeric

Enter the records (one attribute per line, separated by spaces):
Record 1: red 5
Record 2: blue 10
Record 3: green 7

Dissimilarity between pairs of records:
Dissimilarity between Record 1 and Record 2: 1.5000
Dissimilarity between Record 1 and Record 3: 1.2000
Dissimilarity between Record 2 and Record 3: 1.4000


'''

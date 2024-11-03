'''
Step-by-Step Algorithm for Decision Tree Implementation
Input:
Training data with attributes (age, income, student, credit_rating)
Target variable (class_buys_computer)
Steps:
Load Training Data

Read CSV file containing training examples
Store data as list of dictionaries
Each dictionary contains attribute values and class label
Calculate Entropy (S)

Count total examples (N)
Count positive examples (p) and negative examples (n)
Calculate probabilities: p+ = p/N, p- = n/N
Entropy = -p+ log2(p+) - p- log2(p-)
Calculate Information Gain for each Attribute (A)

Get total entropy of dataset (E)
For each possible value (v) of attribute A:
Create subset Sv of examples with A = v
Calculate entropy of subset E(Sv)
Calculate probability p(v) = |Sv|/|S|
Sum weighted entropy: E(A) = Σ p(v) × E(Sv)
Information Gain = E - E(A)
Build Decision Tree

If all examples are positive, return leaf node "yes"
If all examples are negative, return leaf node "no"
If no attributes remain, return majority class
Select best attribute A with highest information gain
Create root node with attribute A
For each possible value v of A:
Create subset Sv of examples with A = v
Recursively build subtree using Sv and remaining attributes
Add subtree as child of root for branch v
Display Tree

Print tree structure with indentation
For each node:
Print attribute name
For each branch:
Print attribute value and subtree/prediction
Make Prediction

Get user input for all attributes
Start at root node
While not at leaf node:
Get attribute A at current node
Get user's value v for attribute A
Follow branch for value v
Return prediction at leaf node
Output:
Decision tree structure
Prediction (yes/no) for new instances


'''

import csv
import math

# Step 1: Read the CSV Data
def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Step 2: Calculate Entropy
def entropy(data):
    total = len(data)
    if total == 0:
        return 0
    count_yes = sum(1 for row in data if row['class_buys_computer'] == 'yes')
    count_no = total - count_yes
    p_yes = count_yes / total
    p_no = count_no / total
    entropy_yes = -p_yes * math.log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no * math.log2(p_no) if p_no > 0 else 0
    # print(f"Entropy: {entropy_yes} + {entropy_no}")
    return entropy_yes + entropy_no

# Step 3: Calculate Information Gain
def information_gain(data, attribute):
    total_entropy = entropy(data)
    values = set(row[attribute] for row in data)
    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    # print(f"Information Gain for {attribute}: {total_entropy} - {weighted_entropy}")
    return total_entropy - weighted_entropy

# Step 4: Split Data
def split_data(data, attribute, value):
    return [row for row in data if row[attribute] == value]

# Step 5: Build Decision Tree
def build_tree(data, attributes):
    if all(row['class_buys_computer'] == 'yes' for row in data):
        return 'yes'
    if all(row['class_buys_computer'] == 'no' for row in data):
        return 'no'
    if not attributes:
        return 'yes' if sum(1 for row in data if row['class_buys_computer'] == 'yes') >= len(data) / 2 else 'no'
    
    best_attribute = max(attributes, key=lambda attr: information_gain(data, attr))
    tree = {best_attribute: {}}
    values = set(row[best_attribute] for row in data)
    for value in values:
        subset = split_data(data, best_attribute, value)
        subtree = build_tree(subset, [attr for attr in attributes if attr != best_attribute])
        tree[best_attribute][value] = subtree
    return tree

# Step 6: Display the Decision Tree
def display_tree(tree, indent=''):
    if isinstance(tree, dict):
        for key, value in tree.items():
            print(f"{indent}{key}")
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    print(f"{indent}  {sub_key} ->")
                    display_tree(sub_value, indent + '    ')
                else:
                    print(f"{indent}  {sub_key} -> {sub_value}")
    else:
        if tree == 'yes':
            print(f"{indent}Predict: Yes")
        else:
            print(f"{indent}Predict: No")

# Step 7: Predict Function
def predict(tree, instance):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = instance[attribute]
    subtree = tree[attribute].get(value, 'no')
    return predict(subtree, instance)

# Step 8: User Input
def get_user_input():
    age = input("Enter age (youth/middle_aged/senior): ")
    income = input("Enter income (high/medium/low): ")
    student = input("Are you a student? (yes/no): ")
    credit_rating = input("Enter credit rating (fair/excellent): ")
    return {'age': age, 'income': income, 'student': student, 'credit_rating': credit_rating}

# Step 9: Make Prediction
def main():
    data = load_data('Data/DesicionTree.csv')
    attributes = ['age', 'income', 'student', 'credit_rating']
    tree = build_tree(data, attributes)
    display_tree(tree)
    instance = get_user_input()
    prediction = predict(tree, instance)
    print(f"Prediction for class_buys_computer: {prediction}")

if __name__ == "__main__":
    main()
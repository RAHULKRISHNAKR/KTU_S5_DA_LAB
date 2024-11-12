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

# Function to load data from a CSV file
def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        # Use DictReader to read the CSV into a list of dictionaries
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to calculate entropy of the dataset
def entropy(data):
    total = len(data)
    if total == 0:
        return 0
    # Count positive and negative instances
    count_yes = sum(1 for row in data if row['class_buys_computer'] == 'yes')
    count_no = total - count_yes
    # Calculate probabilities
    p_yes = count_yes / total
    p_no = count_no / total
    # Calculate entropy components
    entropy_yes = -p_yes * math.log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no * math.log2(p_no) if p_no > 0 else 0
    # Total entropy
    return entropy_yes + entropy_no

# Function to calculate information gain of an attribute
def information_gain(data, attribute):
    total_entropy = entropy(data)
    # Get unique values of the attribute
    values = set(row[attribute] for row in data)
    weighted_entropy = 0
    # Calculate weighted entropy for each value
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        p = len(subset) / len(data)
        weighted_entropy += p * entropy(subset)
    # Information gain is the difference between total entropy and weighted entropy
    return total_entropy - weighted_entropy

# Function to split the data based on an attribute and its value
def split_data(data, attribute, value):
    return [row for row in data if row[attribute] == value]

# Function to build the decision tree
def build_tree(data, attributes):
    # If all instances have the same class, return that class
    if all(row['class_buys_computer'] == 'yes' for row in data):
        return 'yes'
    if all(row['class_buys_computer'] == 'no' for row in data):
        return 'no'
    # If no attributes left, return the majority class
    if not attributes:
        count_yes = sum(1 for row in data if row['class_buys_computer'] == 'yes')
        return 'yes' if count_yes >= len(data) / 2 else 'no'
    
    # Select the best attribute based on information gain
    gains = [(attr, information_gain(data, attr)) for attr in attributes]
    best_attribute, best_gain = max(gains, key=lambda x: x[1])
    # Create a subtree for the best attribute
    tree = {best_attribute: {}}
    values = set(row[best_attribute] for row in data)
    # Build subtree for each value of the best attribute
    for value in values:
        subset = split_data(data, best_attribute, value)
        remaining_attributes = [attr for attr in attributes if attr != best_attribute]
        subtree = build_tree(subset, remaining_attributes)
        tree[best_attribute][value] = subtree
    return tree

# Function to display the decision tree
def display_tree(tree, indent=''):
    if isinstance(tree, dict):
        # Get the attribute to split on
        attribute = next(iter(tree))
        print(f"{indent}{attribute}")
        for value, subtree in tree[attribute].items():
            print(f"{indent}  {value} -> ", end='')
            # Recursively display the subtree
            display_tree(subtree, indent + '    ')
    else:
        # Leaf node
        print(f"{tree}")

# Function to predict the class label for a given instance
def predict(tree, instance):
    if not isinstance(tree, dict):
        # If it's a leaf node, return the class label
        return tree
    # Get the attribute to split on
    attribute = next(iter(tree))
    # Get the value of the attribute for the instance
    value = instance[attribute]
    subtree = tree[attribute].get(value)
    if subtree is None:
        # If the value is not in the subtree, return 'no' or handle accordingly
        return 'no'
    # Recursively predict the class label
    return predict(subtree, instance)

# Function to get user input for prediction
def get_user_input():
    print("Please provide the following information:")
    age = input("Enter age (youth/middle_aged/senior): ").strip()
    income = input("Enter income (high/medium/low): ").strip()
    student = input("Are you a student? (yes/no): ").strip()
    credit_rating = input("Enter credit rating (fair/excellent): ").strip()
    return {'age': age, 'income': income, 'student': student, 'credit_rating': credit_rating}

# Main function to execute the steps
def main():
    # Load data from CSV
    data = load_data('Data/DecisionTree.csv')
    # Define the attributes
    attributes = ['age', 'income', 'student', 'credit_rating']
    # Build the decision tree
    tree = build_tree(data, attributes)
    print("Decision Tree:")
    display_tree(tree)
    # Get user input for prediction
    instance = get_user_input()
    # Predict the class label
    prediction = predict(tree, instance)
    print(f"\nPrediction for class_buys_computer: {prediction}")

if __name__ == "__main__":
    main()
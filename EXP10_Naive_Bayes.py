'''
Step-by-Step Algorithm for Naive Bayes Classifier
Input:
Training data with features (Feature1, Feature2)
Target variable (Class)
Test instance for prediction
Steps:
Load and Preprocess Data

Read CSV file into DataFrame
Extract features and target variables
Store features as numpy array
Store target/class labels as numpy array
Calculate Prior Probabilities

Find unique classes in target variable
Count occurrences of each class
Calculate prior probability for each class:
P(class) = count(class) / total_samples
Calculate Likelihood Probabilities

For each class:
Select features where target equals current class
For each feature:
Find unique values and their counts
Calculate likelihood for each value:
P(feature|class) = count(feature_value) / count(class)
Store likelihoods in dictionary
Get Test Instance

Accept user input for test features
Validate input format
Convert input to numpy array
Calculate Posterior Probabilities

For each class:
Calculate log of prior probability
For each feature in test instance:
Get likelihood from stored values
Add log of likelihood to running sum
Calculate posterior = log(prior) + sum(log(likelihoods))
Store posterior probability
Make Prediction

Find class with maximum posterior probability
Return predicted class
'''

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Data/Naive_Bayes.csv')

# Preprocess the data
# Extract features (Feature1, Feature2) and target (Class) from the DataFrame
features = df[['Feature1', 'Feature2']].values
target = df['Class'].values

# Calculate prior probabilities for each class
classes, class_counts = np.unique(target, return_counts=True)
priors = class_counts / len(target)

# Calculate likelihoods for each feature per class
likelihoods = {}
for cls in classes:
    # Select rows where the class is equal to the current class
    class_features = features[target == cls]
    likelihoods[cls] = {}
    for feature_index in range(features.shape[1]):
        # Initialize a dictionary to store the likelihoods for the current feature
        feature_likelihoods = {}
        # Calculate the frequency of each feature value for the current class
        feature_values, feature_counts = np.unique(class_features[:, feature_index], return_counts=True)
        for value, count in zip(feature_values, feature_counts):
            # Calculate the likelihood of each feature value for the current class
            feature_likelihoods[value] = count / len(class_features)
        # Store the likelihoods for the current feature in the likelihoods dictionary
        likelihoods[cls][feature_index] = feature_likelihoods

# User input for test data
while True:
    user_input = input("Enter test data (Feature1, Feature2) or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break
    user_features = user_input.split(',')
    if len(user_features) != 2:
        print("Invalid input. Please enter two features separated by a comma.")
        continue

    # Convert user input to a NumPy array
    user_features = np.array(user_features).reshape(1, -1)
    posteriors = []
    for idx, cls in enumerate(classes):
        # Calculate the prior probability for the current class
        prior = np.log(priors[idx])
        likelihood = 0
        for feature_index in range(features.shape[1]):
            # Calculate the likelihood of the user input features for the current class
            if user_features[0, feature_index] in likelihoods[cls][feature_index]:
                likelihood += np.log(likelihoods[cls][feature_index][user_features[0, feature_index]])
            else:
                likelihood += np.log(1e-6)  # Smoothing for unseen feature values
        # Calculate the posterior probability for the current class
        posterior = prior + likelihood
        posteriors.append(posterior)
    # Predict the class with the highest posterior probability
    prediction = classes[np.argmax(posteriors)]
    print(f"Predicted Class: {prediction}")
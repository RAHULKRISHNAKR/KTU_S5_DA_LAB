'''
________________________________Algorithm_____________________________________________________

Input:
A dataset of input features and target outputs
Neural network structure (number of neurons in input, hidden, and output layers)
Learning rate
Number of epochs
Steps:
Initialize Weights and Biases

Randomly initialize weights and biases for the hidden and output layers
Define Activation Functions

Define the sigmoid activation function
Define the derivative of the sigmoid function
Forward Propagation

For each epoch:
Calculate the activation of the hidden layer:
Compute the dot product of inputs and hidden weights
Add hidden biases
Apply the sigmoid activation function
Calculate the activation of the output layer:
Compute the dot product of hidden layer output and output weights
Add output biases
Apply the sigmoid activation function
Calculate Error

Compute the difference between the target output and the predicted output
Backpropagation

Calculate the gradient for the output layer:
Compute the derivative of the error with respect to the predicted output
Multiply by the derivative of the sigmoid function applied to the predicted output
Calculate the error and gradient for the hidden layer:
Compute the dot product of the output layer gradient and the transpose of the output weights
Multiply by the derivative of the sigmoid function applied to the hidden layer output
Update Weights and Biases

Update the weights and biases for the output layer:
Adjust output weights by adding the dot product of the hidden layer output transpose and the output layer gradient, scaled by the learning rate
Adjust output biases by adding the sum of the output layer gradient, scaled by the learning rate
Update the weights and biases for the hidden layer:
Adjust hidden weights by adding the dot product of the input transpose and the hidden layer gradient, scaled by the learning rate
Adjust hidden biases by adding the sum of the hidden layer gradient, scaled by the learning rate
Print Output

After every 1000 epochs, print the current epoch, predicted output, and error
Final Output

Print the final hidden weights, hidden biases, output weights, output biases, and the predicted output after the last epoch
Output:
Final weights and biases for the hidden and output layers
Predicted output from the neural network after training
Example:
Input: XOR dataset, learning rate = 0.1, epochs = 10000
Output: Final weights, biases, and predicted output
Notes:
Adjust the number of neurons, learning rate, and epochs based on your specific problem and dataset.
Ensure the dataset is in the correct format (input features and target outputs).
_____________________________________________________________________________________
'''

import numpy as np

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network structure
input_layer_neurons = 2  # Number of features in the dataset (e.g., XOR input)
hidden_layer_neurons = 2  # Number of neurons in the hidden layer
output_neurons = 1  # Number of neurons in the output layer (e.g., XOR output)

# Initialize weights and biases
# Randomly initialize weights and biases for the hidden and output layers
np.random.seed(42)
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# Define the learning rate and number of epochs
learning_rate = 0.1
epochs = 10000

# Define the input features and target output for the XOR problem
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_output = np.array([[0], [1], [1], [0]])

# Train the neural network
for epoch in range(epochs):
    # Forward propagation
    # Calculate the activation of the hidden layer
    hidden_layer_activation = np.dot(inputs, hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    # Calculate the activation of the output layer
    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)

    # Calculate the error
    error = target_output - predicted_output

    # Backpropagation
    # Calculate the gradient for the output layer
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    # Calculate the error and gradient for the hidden layer
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    # Update the weights and biases for the output layer
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    # Update the weights and biases for the hidden layer
    hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print output after every 1000 epochs
    if (epoch + 1) % 1000 == 0:
        print(f"Epoch {epoch + 1}")
        print("Predicted Output: \n", predicted_output)
        print("Error: \n", error)
        print("\n")

# Test the neural network
print("Final hidden weights: ", hidden_weights)
print("Final hidden bias: ", hidden_bias)
print("Final output weights: ", output_weights)
print("Final output bias: ", output_bias)

print("\nOutput from neural network after 10,000 epochs: ")
print(predicted_output)
import numpy as np
#Single Neuron

inputs = [2, 3]
weights = [0.4, 0.7]
bias = 0.5

z = np.dot(inputs, weights) + bias

#ReLU
def relu(x):
    return max(0, x)

print(f"Weighted Sum : {z:.2f}")
print(f"Output after ReLU: {relu(z):.2f}")


#Tiny neural network
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([1, 2])
print(f"Input layer values: {x}")

w_hidden = np.array([
    [0.5, 0.3],
    [0.4, 0.7]
])

b_hidden = np.array([0.1, 0.2])

z_hidden = np.dot(w_hidden, x) + b_hidden
print(f"Weighted Sum of hidden layer: {z_hidden}")

a_hidden = relu(z_hidden)

print(f"Hidden layer outputs: {a_hidden}")

w_output = np.array([0.6, 0.9])
b_output = 0.3

z_output = np.dot(w_output, a_hidden) + b_output
print(f"Weighted Sum of output layer: {z_output}")

prediction = sigmoid(z_output)
print(f"Final Prediction: {prediction}")

print(f"Probability: {prediction*100:.2f}%")



#Experiment with activation functions

x = np.array([-4, -2, 0, 2, 4])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha = 0.01):
    return np.where(x>0, x, alpha * x)

print(f"Sigmoid value: {sigmoid(x)}")
print(f"ReLU value: {relu(x)}")
print(f"Leaky ReLU value: {leaky_relu(x)}")
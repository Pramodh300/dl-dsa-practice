from matplotlib.pyplot import bar_label
import numpy as np
import matplotlib.pyplot as plt

#sigmoid

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-5, -2, 0, 2, 5])
print(sigmoid(x))


#ReLU
def relu(x):
    return np.maximum(0, x)

x = np.array([-5, -2, 0, 2, 5])
print(relu(x))



#Softmax
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

scores = np.array([2.0, 4.0, 1.0])
print(softmax(scores))


#Plot the outputs of all three functions using Matplotlib
plt.plot(x, sigmoid(x))
plt.show()

plt.plot(x ,relu(x))
plt.show()

plt.plot(scores, softmax(scores))
plt.show()


#using numpy
x = np.array([-3, -1, 0, 1, 3])
def sigmoid(x):
    return 1/ (1 - np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha = 0.01):
    return np.where(x>0, x, alpha * x)

print(sigmoid(x))
print(relu(x))
print(leaky_relu(x))
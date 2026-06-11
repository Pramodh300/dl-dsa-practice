#Build a Single Artificial Neuron
hours = 6
attendence = 90
assignements = 85

w1 = 0.5
w2 = 0.2
w3 = 0.3

b = 2
z = (hours * w1) + (attendence * w2) + (assignements * w3) + b

print(f"Weighted sum: ",z)


#Add a Step Activation Function
def activation(z):
    if z >= 25:
        return 1
    else:
        return 0

hours = 6
attendence = 90
assignements = 85

w1 = 0.5
w2 = 0.2
w3 = 0.3

b = 2

z = (hours * w1) + (attendence * w2) + (assignements * w3) + b

output = activation(z)
print("Weighted sum: ",z)
print("Prediction: ",output)

if output == 1:
    print("Student will pass")
else:
    print("Student will fail")



#Build a Reusable Perceptron Function
def perceptron(inputs, weights, bias):

    sum = 0

    for input, weight in zip(inputs, weights):
        sum = sum + (input * weight)

    total = sum + bias

    if total >= 25:
        return 1
    else:
        return 0


inputs = [3, 20, 55]
weights = [0.5, 0.2, 0.3]
bias = 2

output = perceptron(inputs, weights, bias)

print(f"Prediction: {output}")

if output == 1:
    print("Student will pass")
else:
    print("Student will fail")



#Use NumPy Dot Product
import numpy as np

def perceptron(inputs, weights, bias):

    total = np.dot(inputs, weights) + bias

    if total >= 25:
        return 1

    else:
        return 0

inputs = [6, 90, 85]
weights = [0.5, 0.2, 0.3]
bias = 2

output = perceptron(inputs, weights, bias)

print(f"Prediction: {output}")

if output == 1:
    print("Student will pass")
else:
    print("Student will fail")
#One Learning Step
import numpy as np

# Input
x = 2

# Initial weight and bias
w = 3.0
b = 1.0

# Target value
y_true = 5

# Learning rate
lr = 0.1

# -----------------------------
# Forward Propagation
# -----------------------------
z = w * x + b
y_pred = z

# Loss (Mean Squared Error)
loss = (y_true - y_pred) ** 2

# -----------------------------
# Backpropagation
# -----------------------------

# dL/dy_pred
dL_dy = 2 * (y_pred - y_true)

# dy_pred/dw
dy_dw = x

# Chain Rule
dL_dw = dL_dy * dy_dw

# Weight Update
w = w - lr * dL_dw

print("Prediction :", y_pred)
print("Loss       :", loss)
print("Gradient   :", dL_dw)
print("Updated Weight :", w)


#Multiple Training Epochs
import numpy as np

x = 2
y_true = 5

w = 3.0
b = 1.0

learning_rate = 0.1

for epoch in range(10):

    # Forward Pass
    y_pred = w * x + b
    loss = (y_true - y_pred) ** 2

    # Backward Pass
    dL_dy = 2 * (y_pred - y_true)
    dL_dw = dL_dy * x

    # Update
    w = w - learning_rate * dL_dw

    print(f"Epoch {epoch+1}")
    print(f"Prediction: {y_pred:.4f}")
    print(f"Loss: {loss:.4f}")
    print(f"Weight: {w:.4f}")
    print("-" * 30)


'''Day 66: Backpropagation and Chain Rule (Theory Notes)
1. Introduction

A neural network learns by repeatedly making predictions, measuring its errors, and adjusting its internal parameters (weights and biases) to reduce those errors. This learning process is achieved through Backpropagation, one of the most fundamental algorithms in Deep Learning.

Backpropagation works together with Forward Propagation and Gradient Descent to train a neural network.

The complete learning cycle of a neural network is:

Input Data
     ↓
Forward Propagation
     ↓
Prediction
     ↓
Loss Calculation
     ↓
Backpropagation
     ↓
Weight Update
     ↓
Repeat
2. What is Backpropagation?
Definition

Backpropagation (Backward Propagation of Errors) is the algorithm used to compute how much each weight and bias in a neural network contributed to the final prediction error. Using this information, the network adjusts its parameters to reduce the error during future predictions.

In simple words:

Forward Propagation determines what the network predicts.
Backpropagation determines how the network should change its weights to improve the prediction.

Thus, backpropagation is the learning mechanism of neural networks.

3. Intuition Behind Backpropagation

Consider a student preparing for an exam. After writing a mock test, the student checks the mistakes, identifies weak areas, studies those topics, and performs better in the next test.

Similarly, a neural network:

Makes a prediction.
Compares the prediction with the correct answer.
Calculates the error.
Determines which weights caused the error.
Slightly adjusts those weights.
Makes a better prediction next time.

Backpropagation is essentially the process of learning from mistakes.

4. Components of Neural Network Learning

Training a neural network consists of four major stages:

Step	Description
1. Forward Propagation	Pass the input through the network and generate a prediction.
2. Loss Calculation	Measure how different the prediction is from the true value.
3. Backpropagation	Calculate the gradients (partial derivatives) of the loss with respect to each weight.
4. Weight Update	Update the weights using Gradient Descent to reduce future errors.

This process is repeated for many iterations (epochs) until the network achieves satisfactory performance.

5. What is a Loss Function?

A neural network requires a mathematical method to measure how wrong its prediction is. This measure is called the Loss Function (or Cost Function).

The loss function compares the predicted output with the actual output and produces a numerical value representing the prediction error.

Example

Suppose a model predicts the price of a house.

Actual Price	Predicted Price
100	90

The prediction error is:

Error=Actual Value−Predicted Value
Error=100−90=10

A larger error indicates a poorer prediction, while a smaller error indicates a better prediction.

6. Mean Squared Error (MSE)

For regression problems, one of the most commonly used loss functions is Mean Squared Error (MSE).

MSE=
n
1
	​

i=1
∑
n
	​

(y
i
	​

−
y
^
	​

i
	​

)
2

Where:

n = number of training examples.
y
i
	​

 = actual (true) value.
y
^
	​

i
	​

 = predicted value.
Why do we square the error?

Squaring the error provides two important benefits:

Positive and negative errors cannot cancel each other.
Larger errors are penalized more heavily than smaller errors.
Example

Suppose:

Actual value = 5
Predicted value = 3

Then,

Loss=(5−3)
2
=2
2
=4

A perfect prediction would produce a loss of zero.

7. Objective of Training

The primary goal of training a neural network is to minimize the loss function.

Large Loss → Poor prediction.
Small Loss → Good prediction.
Zero Loss → Perfect prediction.

The challenge is determining which weights should increase or decrease to reduce the loss. This is solved using gradients.

8. What is a Gradient?

A gradient measures how much the loss changes when a parameter (such as a weight) changes slightly.

Mathematically, the gradient is the partial derivative of the loss with respect to a parameter:

∂w
∂L
	​


where:

L = Loss,
w = Weight.

A gradient answers the question:

"If I change this weight a little, how will the loss change?"

Mountain Analogy

Imagine standing on a mountain and trying to reach the lowest valley.

The top of the mountain represents high loss.
The bottom of the valley represents minimum loss.

The gradient points toward the direction of the steepest increase. Therefore, to minimize the loss, we move in the opposite direction of the gradient.

9. Gradient Descent

Gradient Descent is the optimization algorithm used to update the weights of a neural network.

The update rule is:

w
new
	​

=w
old
	​

−η
∂w
∂L
	​


Where:

w
new
	​

 = updated weight,
w
old
	​

 = current weight,
η = learning rate,
∂w
∂L
	​

 = gradient.

The subtraction sign indicates that we move opposite to the gradient direction because we want to minimize the loss.

10. Learning Rate

The learning rate (denoted by η) controls the size of each weight update during training.

If the learning rate is too small:
Learning becomes very slow.
The model requires many iterations to converge.
If the learning rate is too large:
The model may overshoot the optimal solution.
Training can become unstable and may never converge.

Typical learning rate values include:

0.1
0.01
0.001

Choosing an appropriate learning rate is crucial for successful training.

11. The Chain Rule

The mathematical foundation of backpropagation is the Chain Rule from calculus.

Suppose:

y=(2x+3)
2

Let:

u=2x+3

Then:

y=u
2

The chain rule states:

dx
dy
	​

=
du
dy
	​

×
dx
du
	​

Interpretation

To determine how a small change in x affects y, we multiply:

The effect of u on y.
The effect of x on u.

Backpropagation repeatedly applies this principle through every layer of a neural network.

12. Chain Rule Numerical Example

Given:

x=2

Then:

u=2(2)+3=7
y=7
2
=49
Step 1: Compute 
du
dy
	​

du
dy
	​

=2u=14
Step 2: Compute 
dx
du
	​

dx
du
	​

=2
Step 3: Apply the Chain Rule
dx
dy
	​

=
du
dy
	​

×
dx
du
	​

=14×2=28

Thus,

dx
dy
	​

=28

This multiplication of derivatives is exactly how backpropagation computes gradients.

13. Forward and Backward Pass Example

Consider a simple neuron.

Given:
Input: x=2
Weight: w=3
Bias: b=1
Step 1: Forward Propagation

The neuron computes:

z=wx+b

Substituting the values:

z=(3)(2)+1=7

Prediction:

y
^
	​

=7

Suppose the true target value is:

y=5
Step 2: Loss Calculation

Using squared error:

L=(y−
y
^
	​

)
2
L=(5−7)
2
=4
Step 3: Backpropagation

We want to know:

How much does changing the weight affect the loss?

Using the chain rule:

∂w
∂L
	​

=
∂z
∂L
	​

×
∂w
∂z
	​

First derivative:

Since:

L=(5−z)
2
∂z
∂L
	​

=2(z−5)

Substitute z=7:

2(7−5)=4
Second derivative:

Since:

z=wx+b
∂w
∂z
	​

=x=2
Apply Chain Rule:
∂w
∂L
	​

=4×2=8

Thus, the gradient is:

∂w
∂L
	​

=8
14. Weight Update

Suppose:

Current weight = 3,
Learning rate = 0.1.

Using Gradient Descent:

w
new
	​

=w
old
	​

−η
∂w
∂L
	​


Substitute the values:

w
new
	​

=3−0.1(8)
w
new
	​

=3−0.8=2.2

Thus, the weight is updated from:

3.0→2.2

The updated weight should produce a prediction closer to the target value during the next forward pass.

15. Why Does Backpropagation Work?

Modern deep neural networks may contain:

Millions or even billions of weights.
Dozens or hundreds of layers.

Manually adjusting each weight is impossible.

Backpropagation efficiently computes the gradients for all trainable parameters simultaneously by repeatedly applying the chain rule from the output layer back to the input layer.

Without backpropagation, training modern AI models such as:

GPT,
BERT,
ResNet,
Stable Diffusion,
AlphaGo,

would not be computationally feasible.

16. Relationship Between Forward Propagation and Backpropagation
Forward Propagation	Backpropagation
Computes predictions.	Computes gradients.
Moves from input layer to output layer.	Moves from output layer back to input layer.
Uses current weights and biases.	Updates weights and biases.
Produces output values.	Reduces prediction error.
17. Summary
A neural network first performs Forward Propagation to generate a prediction.
The prediction is compared with the true value using a Loss Function.
Backpropagation computes the contribution of each weight to the loss using the Chain Rule.
Gradients indicate how each weight should change.
Gradient Descent updates the weights in the direction that minimizes the loss.
This process is repeated many times until the network learns an effective mapping from inputs to outputs.
Key Definitions (Quick Revision)
Term	Definition
Forward Propagation	Process of passing input through the network to generate a prediction.
Loss Function	Mathematical function that measures prediction error.
Gradient	Rate of change of the loss with respect to a parameter.
Backpropagation	Algorithm that computes gradients using the chain rule.
Chain Rule	Calculus rule for differentiating composite functions.
Gradient Descent	Optimization algorithm used to update weights and minimize loss.
Learning Rate	Hyperparameter controlling the size of each weight update.
One-Line Memory Formula

Forward Propagation makes a prediction → Loss measures the error → Backpropagation computes the gradients → Gradient Descent updates the weights → The network learns.
'''
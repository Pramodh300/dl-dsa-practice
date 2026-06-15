import numpy as np

# ======================================================
# 1. DATASET (XOR Problem)
# ======================================================

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# ======================================================
# 2. INITIALIZE WEIGHTS AND BIASES
# ======================================================

np.random.seed(42)   # For reproducible results

# Input Layer (2 neurons) -> Hidden Layer (3 neurons)
W1 = np.random.randn(2, 3)
b1 = np.zeros((1, 3))

# Hidden Layer (3 neurons) -> Output Layer (1 neuron)
W2 = np.random.randn(3, 1)
b2 = np.zeros((1, 1))

# ======================================================
# 3. ACTIVATION FUNCTIONS
# ======================================================

# ReLU Activation
def relu(x):
    return np.maximum(0, x)

# ReLU Derivative
def relu_derivative(x):
    return (x > 0).astype(float)

# Sigmoid Activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Sigmoid Derivative
def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# ======================================================
# 4. TRAINING PARAMETERS
# ======================================================

learning_rate = 0.1
epochs = 10000
m = X.shape[0]       # Number of training examples

# ======================================================
# 5. TRAINING LOOP
# ======================================================

for epoch in range(epochs):

    # --------------------------------------------------
    # FORWARD PROPAGATION
    # --------------------------------------------------

    # Hidden Layer
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)

    # Output Layer
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    # --------------------------------------------------
    # LOSS CALCULATION (Binary Cross Entropy)
    # --------------------------------------------------

    loss = -np.mean(
        y * np.log(A2 + 1e-8) +
        (1 - y) * np.log(1 - A2 + 1e-8)
    )

    # --------------------------------------------------
    # BACKPROPAGATION
    # --------------------------------------------------

    # Output layer gradients
    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    # Hidden layer gradients
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * relu_derivative(Z1)

    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    # --------------------------------------------------
    # GRADIENT DESCENT (UPDATE WEIGHTS)
    # --------------------------------------------------

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1

    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    # --------------------------------------------------
    # PRINT LOSS EVERY 1000 EPOCHS
    # --------------------------------------------------

    if epoch % 1000 == 0:
        print(f"Epoch {epoch:5d} | Loss: {loss:.6f}")

# ======================================================
# 6. FINAL RESULTS
# ======================================================

print("\n==============================")
print("Training Complete!")
print("==============================")

print("\nFinal Weights and Biases:")
print("\nW1:")
print(W1)

print("\nb1:")
print(b1)

print("\nW2:")
print(W2)

print("\nb2:")
print(b2)

# ======================================================
# 7. MAKE FINAL PREDICTIONS
# ======================================================

# Forward pass one final time
Z1 = np.dot(X, W1) + b1
A1 = relu(Z1)

Z2 = np.dot(A1, W2) + b2
A2 = sigmoid(Z2)

print("\n==============================")
print("Predicted Probabilities")
print("==============================")
print(A2)

print("\n==============================")
print("Rounded Predictions")
print("==============================")
print(np.round(A2))

print("\n==============================")
print("Actual Labels")
print("==============================")
print(y)
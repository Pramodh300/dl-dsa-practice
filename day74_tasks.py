import torch
import torch.nn as nn
'''
class CustomNeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        # Always call the superclass constructor to initialize PyTorch's internal states
        super(CustomNeuralNetwork, self).__init__()
        
        # Define layer 1: Map input features to a hidden dimension space
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        
        # Define the non-linear activation layer
        self.activation = nn.ReLU()
        
        # Define layer 2: Map hidden features to the final output dimension space
        self.layer2 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # Pass input through the first linear layer
        x = self.layer1(x)
        
        # Apply the element-wise ReLU activation function
        x = self.activation(x)
        
        # Pass the result through the final linear layer
        out = self.layer2(x)
        return out

# --- Verification and Execution ---
# Instantiate our network (e.g., 10 input elements, 32 hidden nodes, 2 output classes)
model = CustomNeuralNetwork(input_dim=10, hidden_dim=32, output_dim=2)
print("Model Structural Architecture:\n", model)

# Create a dummy data batch representing 5 samples, each with 10 features
dummy_input = torch.randn(5, 10)

# Execute the forward pass through the callable instance interface
predictions = model(dummy_input)
print("\nOutput Shape (Expected: [5, 2]):", predictions.shape)



#nn.Linear(3,1)
layer = nn.Linear(3,1)
print("Weights: ")
print(layer.weight)

print("Bias: ")
print(layer.bias)



#ReLU
relu = nn.ReLU()
x = torch.tensor([5.0, -5.0, 10.0, -10.0])
output = relu(x)
print("Input: ")
print(x)

print("Output: ")
print(output)
'''


#StudentNet Class
class StudentNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(3, 5)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(5, 1)


    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)

        return x

model = StudentNet()

print(model)
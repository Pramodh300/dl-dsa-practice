import torch
import numpy as np

print("PyTorch Version:", torch.__version__)

# Tensor Creation
x = torch.tensor([
    [1,2],
    [3,4]
])

print("\nTensor:")
print(x)

print("\nShape:")
print(x.shape)

# Operations
a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])

print("\nAddition:")
print(a+b)

print("\nMultiplication:")
print(a*b)

# NumPy Bridge
arr = np.array([10,20,30])

tensor = torch.from_numpy(arr)

print("\nNumPy to Tensor:")
print(tensor)

# GPU
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("\nDevice:")
print(device)

tensor = tensor.to(device)

print("\nTensor on Device:")
print(tensor)
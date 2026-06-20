#Practice problem
import torch

x = torch.tensor(0.0, requires_grad=True)  # start with x = 0
learning_rate = 0.1

print("Finding the minimum of z = (x-5)²")
print("-" * 40)

for step in range(20):

    # STEP 1: Forward — compute z
    z = (x - 5) ** 2

    # STEP 2: Backward — compute dz/dx
    z.backward()

    # STEP 3: Update x to reduce z
    with torch.no_grad():          # don't track this update
        x -= learning_rate * x.grad  # move x in direction that reduces z

    # STEP 4: Zero the gradient
    x.grad.zero_()

    if step % 4 == 0:
        print(f"Step {step:2d}: x = {x.item():.4f}, z = {z.item():.4f}")

print(f"\nFinal x = {x.item():.4f}  (should be 5.0)")



#Practice problem 2
x = torch.tensor(3.0, requires_grad=True)  # start with x = 0
learning_rate = 0.1

print("Finding the minimum of z = (x-12)²")
print("-" * 40)

for step in range(20):

    # STEP 1: Forward — compute z
    z = (x - 12) ** 2

    # STEP 2: Backward — compute dz/dx
    z.backward()

    # STEP 3: Update x to reduce z
    with torch.no_grad():          # don't track this update
        x -= learning_rate * x.grad  # move x in direction that reduces z

    # STEP 4: Zero the gradient
    x.grad.zero_()

    if step % 4 == 0:
        print(f"Step {step:2d}: x = {x.item():.4f}, z = {z.item():.4f}")

print(f"\nFinal x = {x.item():.4f}  (should be 12.0)")
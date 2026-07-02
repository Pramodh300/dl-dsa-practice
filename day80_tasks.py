import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# -------------------------------------------------
# Step 1 : Device Configuration
# -------------------------------------------------

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(device)

# -------------------------------------------------
# Step 2 : Image Transform
# -------------------------------------------------

transform = transforms.Compose([
    transforms.ToTensor(),

    transforms.Normalize(
        mean=(0.5, 0.5, 0.5),
        std=(0.5, 0.5, 0.5)
    )
])

# -------------------------------------------------
# Step 3 : Load Dataset
# -------------------------------------------------

train_dataset = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.CIFAR10(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

# -------------------------------------------------
# Step 4 : DataLoader
# -------------------------------------------------

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)

# -------------------------------------------------
# Step 5 : CNN Model
# -------------------------------------------------

class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        # First Convolution Block
        self.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        self.relu1 = nn.ReLU()

        self.pool1 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )

        # Second Convolution Block
        self.conv2 = nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=3,
            padding=1
        )

        self.relu2 = nn.ReLU()

        self.pool2 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )

        # Fully Connected Layers

        self.fc1 = nn.Linear(
            64 * 8 * 8,
            512
        )

        self.relu3 = nn.ReLU()

        self.fc2 = nn.Linear(
            512,
            10
        )

    def forward(self, x):

        # Conv Block 1

        x = self.conv1(x)

        x = self.relu1(x)

        x = self.pool1(x)

        # Conv Block 2

        x = self.conv2(x)

        x = self.relu2(x)

        x = self.pool2(x)

        # Flatten

        x = x.view(x.size(0), -1)

        # Fully Connected

        x = self.fc1(x)

        x = self.relu3(x)

        x = self.fc2(x)

        return x


# -------------------------------------------------
# Step 6 : Create Model
# -------------------------------------------------

model = CNN().to(device)

# -------------------------------------------------
# Step 7 : Loss Function
# -------------------------------------------------

criterion = nn.CrossEntropyLoss()

# -------------------------------------------------
# Step 8 : Optimizer
# -------------------------------------------------

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# -------------------------------------------------
# Step 9 : Training Loop
# -------------------------------------------------

epochs = 10

for epoch in range(epochs):

    model.train()

    running_loss = 0

    for images, labels in train_loader:

        images = images.to(device)

        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{epochs} "
        f"Loss : {running_loss/len(train_loader):.4f}"
    )

# -------------------------------------------------
# Step 10 : Testing
# -------------------------------------------------

model.eval()

correct = 0

total = 0

with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)

        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"Test Accuracy : {accuracy:.2f}%")

# -------------------------------------------------
# Step 11 : Save Model
# -------------------------------------------------

torch.save(
    model.state_dict(),
    "cnn_model.pth"
)

print("Model Saved Successfully")
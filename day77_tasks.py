import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Device: ",device)

transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root = "data",
    download= True,
    train = True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root = "data",
    download=True,
    train = False,
    transform=transform    
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size = 64,
    shuffle = False
)

class DigitClassifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu1 = nn.ReLU()

        self.fc2 = nn.Linear(128,64)
        self.relu2 = nn.ReLU()

        self.fc3 = nn.Linear(64, 10)

    def forward(self,x):
        x = x.view(-1,28*28)
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.fc3(x)

        return x
model =DigitClassifier().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(
    model.parameters(),
    lr = 0.001
)

epochs = 5
for epoch in range(epochs):
    model.train()
    running_loss = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch [{epoch + 1}/ {epochs}]"
        f"Loss = {running_loss}"
    )

model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, prediction = torch.max(outputs, 1)
        total += labels.size(0)

        correct += (prediction == labels).sum().item()


accuracy = 100 * correct / total
print("Accuracy on test set: ", accuracy)

torch.save(
    model.state_dict(),
    "digit_classifier.pth"
)
print("Model saved successfully")

loaded_model = DigitClassifier().to(device)

loaded_model.load_state_dict(
    torch.load(
        "digit_classifier.pth",
        map_location = device
    )
)
loaded_model.eval()
print("Model loaded successfully")

image, label = test_dataset[0]
image = image.unsqueeze(0).to(device)

with torch.no_grad():
    output = loaded_model(image)
    prediction = torch.argmax(output, dim = 1)

print("Acutal label :", label)
print("Predicted label :", prediction.item())
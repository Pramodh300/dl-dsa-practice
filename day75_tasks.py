from torch.utils.data import Dataset, DataLoader
import torch
import torch.nn as nn

#Creating dataset
class EmployeeDataset(Dataset):
    def __init__(self):
        self.features = torch.tensor([
            [1.0, 22.0],
            [3.0, 25.0],
            [5.0, 28.0],
            [7.0, 32.0],
            [10.0, 35.0]
        ])

        # Labels (Salary)
        self.labels = torch.tensor([
            [25000.0],
            [40000.0],
            [60000.0],
            [85000.0],
            [120000.0]
        ])

    
    def __len__(self):
        return len(self.features)

    def __getitem__(self, index):
        return self.features[index], self.labels[index]

dataset = EmployeeDataset()
print("Total Samples: ", len(dataset))

print("Third Samples: ", dataset[2])


#Dataloader
loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

#Creating model
class SalaryPredictor(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x

model = SalaryPredictor()

#Training model

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr = 0.000001
)

epochs = 10

for epoch in range(epochs):
    total_loss = 0
    for X, y in loader:
        optimizer.zero_grad()

        prediction = model(X)
        loss = criterion(prediction, y)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()


    print(f"Epoch {epoch+1}, Loss = {total_loss:.2f}")
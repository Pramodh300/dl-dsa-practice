# ==========================================================
# DAY 83
# Improve CNN Model
# Dropout + BatchNorm + EarlyStopping
# ==========================================================


import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets
from torchvision import transforms

from torch.utils.data import DataLoader
from torch.utils.data import random_split



# ==========================================================
# 1. DEVICE CONFIGURATION
# ==========================================================


device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


print("Using:", device)



# ==========================================================
# 2. IMAGE TRANSFORMATION
# ==========================================================


transform = transforms.Compose([


    # Data augmentation
    transforms.RandomHorizontalFlip(),


    transforms.RandomRotation(10),


    # Convert image to tensor
    transforms.ToTensor(),


    # Normalize RGB channels
    transforms.Normalize(

        mean=(0.5,0.5,0.5),

        std=(0.5,0.5,0.5)

    )

])



# ==========================================================
# 3. LOAD CIFAR10 DATASET
# ==========================================================


dataset = datasets.CIFAR10(

    root="data",

    train=True,

    transform=transform,

    download=True

)



# Split train and validation


train_size = int(
    0.8 * len(dataset)
)


val_size = len(dataset) - train_size



train_dataset, val_dataset = random_split(

    dataset,

    [train_size,val_size]

)



# DataLoader


train_loader = DataLoader(

    train_dataset,

    batch_size=64,

    shuffle=True

)


val_loader = DataLoader(

    val_dataset,

    batch_size=64,

    shuffle=False

)



# ==========================================================
# 4. CREATE CNN MODEL
# ==========================================================



class ImprovedCNN(nn.Module):


    def __init__(self):


        super().__init__()



        # -------------------------
        # Feature extractor
        # -------------------------

        self.features = nn.Sequential(



            # First convolution block


            nn.Conv2d(

                in_channels=3,

                out_channels=32,

                kernel_size=3,

                padding=1

            ),


            nn.BatchNorm2d(32),


            nn.ReLU(),


            nn.MaxPool2d(2),




            # Second convolution block


            nn.Conv2d(

                32,

                64,

                3,

                padding=1

            ),


            nn.BatchNorm2d(64),


            nn.ReLU(),


            nn.MaxPool2d(2),





            # Third convolution block


            nn.Conv2d(

                64,

                128,

                3,

                padding=1

            ),


            nn.BatchNorm2d(128),


            nn.ReLU(),


            nn.MaxPool2d(2)

        )




        # -------------------------
        # Classifier
        # -------------------------


        self.classifier = nn.Sequential(


            nn.Flatten(),



            nn.Linear(

                128*4*4,

                256

            ),


            nn.ReLU(),



            # Dropout layer

            nn.Dropout(0.5),



            nn.Linear(

                256,

                10

            )

        )





    def forward(self,x):


        x = self.features(x)


        x = self.classifier(x)


        return x




model = ImprovedCNN().to(device)



print(model)



# ==========================================================
# 5. LOSS FUNCTION AND OPTIMIZER
# ==========================================================



criterion = nn.CrossEntropyLoss()



optimizer = optim.Adam(

    model.parameters(),

    lr=0.001

)



# ==========================================================
# 6. EARLY STOPPING VARIABLES
# ==========================================================



best_loss = float("inf")


patience = 5


counter = 0



epochs = 50




# ==========================================================
# 7. TRAINING LOOP
# ==========================================================


for epoch in range(epochs):



    # ----------------------
    # Training mode
    # ----------------------

    model.train()


    train_loss = 0



    for images,labels in train_loader:



        images = images.to(device)


        labels = labels.to(device)




        # remove previous gradients

        optimizer.zero_grad()




        # forward propagation

        outputs = model(images)



        # calculate loss

        loss = criterion(

            outputs,

            labels

        )



        # backward propagation

        loss.backward()




        # update weights

        optimizer.step()



        train_loss += loss.item()





    # ----------------------
    # Validation mode
    # ----------------------


    model.eval()



    val_loss = 0


    correct = 0


    total = 0



    with torch.no_grad():



        for images,labels in val_loader:



            images = images.to(device)

            labels = labels.to(device)




            outputs = model(images)



            loss = criterion(

                outputs,

                labels

            )


            val_loss += loss.item()




            _, predicted = torch.max(

                outputs,

                1

            )



            total += labels.size(0)



            correct += (

                predicted == labels

            ).sum().item()





    accuracy = (

        correct / total

    ) * 100





    print(

        f"""
Epoch {epoch+1}

Training Loss: {train_loss:.3f}

Validation Loss: {val_loss:.3f}

Accuracy: {accuracy:.2f} %
        """

    )





    # ======================================================
    # EARLY STOPPING LOGIC
    # ======================================================



    if val_loss < best_loss:



        best_loss = val_loss



        counter = 0



        torch.save(

            model.state_dict(),

            "best_cnn_model.pth"

        )



        print(
            "Model Saved"
        )



    else:



        counter += 1



        print(

            "No Improvement:",

            counter

        )




        if counter >= patience:



            print(
                "Early Stopping Activated"
            )


            break





print("Training Completed")
from flask import Flask, request, jsonify, render_template
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from model import SimpleCNN

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SimpleCNN()
model.load_state_dict(torch.load("model.pth", map_location = device))

model.to(device)

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def predict_image(image):
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probability = F.softmax(output, dim = 1)
        prediction = torch.argmax(
            probability, 1
        ).item()

    return prediction

@app.route("/predict", methods= ["POST"])
def predict():
    file = request.files["image"]
    image = Image.open(file)
    result = predict_image(image)

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug = True)
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load model once
model = tf.keras.models.load_model("dogs_cat_MobileNetV3-FE.keras")

IMG_SIZE = 224  # change to your model input size

def preprocess(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    return image


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    processed_image = preprocess(image)

    prediction = model.predict(processed_image)[0][0]
    print(f"Prediction: {prediction}")  # Debugging output
    
    # Assuming the model outputs a single value for binary classification
    # Adjust the threshold as needed
    label = "Dog" if prediction > 0.5 else "Cat"
    print(f"Label: {label}")  # Debugging output


    # Confidence reflects certainty in the predicted label
    confidence = float(prediction) if label == "Dog" else 1 - float(prediction)
    print(f"Confidence: {confidence}")  # Debugging output

    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": round(confidence, 4),
        "label": label
    })
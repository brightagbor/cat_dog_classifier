
# 🐶🐱 Cat vs Dog Classification (FastAPI + TensorFlow)

This project is a simple **image classification web app** that predicts whether an uploaded image is a **Cat 🐱** or a **Dog 🐶** using a trained **TensorFlow model (MobileNetV3)** and serves predictions via **FastAPI**.

## 🚀 Features

* Upload an image through a web interface
* Classifies image as **Cat** or **Dog**
* Displays prediction with **confidence score**
* Built with:

  * FastAPI (backend)
  * TensorFlow (model inference)
  * Jinja2 (HTML templating)


## 📁 Project Structure

```
.
├── main.py                          # FastAPI application
├── dogs_cat_MobileNetV3-FE.keras   # Trained model
├── templates/
│   └── index.html                  # Frontend UI
├── README.md
```


## ⚙️ Requirements

* Python 3.8+
* TensorFlow
* FastAPI
* Uvicorn
* NumPy
* Pillow (PIL)


## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```


### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn tensorflow numpy pillow jinja2
```

## ▶️ Running the Application

Start the FastAPI server using **Uvicorn**:

```bash
uvicorn main:app --reload
```


## 🌐 Access the App

Open your browser and go to:

```
http://127.0.0.1:8000
```

## 🧪 How It Works

1. User uploads an image
2. Image is resized to **224 × 224**
3. Model makes a prediction
4. Output:

   * **Dog** if prediction > 0.5
   * **Cat** otherwise
5. Confidence score is displayed


## 🧠 Model Details

* Architecture: **MobileNetV3 (Feature Extractor)**
* Input size: `224 x 224`
* Output: Binary classification (Cat vs Dog)


## 📌 API Endpoints

### `GET /`

* Loads the homepage

### `POST /predict`

* Accepts image upload
* Returns prediction + confidence


## ⚠️ Notes

* Ensure the model file:

  ```
  dogs_cat_MobileNetV3-FE.keras
  ```

  is in the root directory.

* The `templates` folder must contain:

  ```
  index.html
  ```

## 🧾 Example Prediction Logic

```python
label = "Dog" if prediction > 0.5 else "Cat"
confidence = prediction if label == "Dog" else 1 - prediction
```

## 🚀 Future Improvements

* Add drag-and-drop upload
* Support multiple image formats
* Deploy to cloud (e.g., Docker, AWS, Render)
* Add model explanation (Grad-CAM)

## 🧠 Summary

This project demonstrates:

* End-to-end ML deployment
* Serving a TensorFlow model via FastAPI
* Simple web-based inference system
# cat_dog_classifier

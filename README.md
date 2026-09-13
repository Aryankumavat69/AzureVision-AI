# 🔷 AzureVision-AI

## AI-Powered Image Analysis Web Application

AzureVision-AI is a full-stack AI image analysis application that allows users to upload an image and receive AI-generated visual classifications with confidence scores.

The project demonstrates an end-to-end AI application workflow combining **Computer Vision, Machine Learning, FastAPI, and a modern web interface**, with deployment planned on Microsoft Azure.

---

## 🚀 Features

* 🖼️ Image upload support
* 📂 Drag & drop image upload
* 👁️ Instant image preview
* 🤖 AI-powered image classification
* 📊 Top-5 prediction results
* 📈 Confidence scores
* ⚡ FastAPI REST API
* 🌐 Responsive web interface
* ❤️ Health-check endpoint
* 📚 Automatic API documentation with Swagger
* ☁️ Azure deployment ready

---

## 🧠 AI Model

The application uses:

**Model:** `google/vit-base-patch16-224`

**Architecture:** Vision Transformer (ViT)

**Framework:** Hugging Face Transformers

The model analyzes an uploaded image and returns the most likely visual categories along with their confidence scores.

---

## 🏗️ System Architecture

```text
                    USER
                     │
                     ▼
            ┌─────────────────┐
            │   Web Frontend  │
            │   HTML/CSS/JS   │
            └────────┬────────┘
                     │
                 Image Upload
                     │
                     ▼
            ┌─────────────────┐
            │     FastAPI     │
            │     Backend     │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  Vision         │
            │  Transformer    │
            │  (ViT)          │
            └────────┬────────┘
                     │
                     ▼
             AI Predictions
             + Confidence %
                     │
                     ▼
            ┌─────────────────┐
            │ Results Dashboard│
            └─────────────────┘
                     │
                     ▼
              Azure Deployment
```

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Drag & Drop API
* Fetch API

### Backend

* Python
* FastAPI
* Uvicorn
* Python Multipart

### Artificial Intelligence

* Hugging Face Transformers
* Vision Transformer (ViT)
* PyTorch
* Torchvision
* Pillow

### Cloud

* Microsoft Azure
* Azure App Service / suitable Azure hosting service

### Development

* Visual Studio Code
* Python Virtual Environment
* Git
* GitHub

---

## 📁 Project Structure

```text
AzureVision-AI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── ai_model.py
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .venv/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Upload Image

The user selects an image or drags and drops one into the application.

### 2. Frontend Processing

JavaScript creates a `FormData` object and sends the image to the FastAPI backend.

### 3. API Processing

FastAPI receives the uploaded image through the `/analyze` endpoint.

### 4. AI Analysis

The image is processed by the Vision Transformer model.

### 5. Prediction

The model generates multiple possible classifications with confidence scores.

### 6. Results

The predictions are returned as JSON and displayed on the web interface using confidence bars.

---

## 🔌 API Endpoints

| Method | Endpoint   | Description               |
| ------ | ---------- | ------------------------- |
| GET    | `/`        | Web application           |
| GET    | `/health`  | API health check          |
| POST   | `/analyze` | Analyze uploaded image    |
| GET    | `/docs`    | Swagger API documentation |

---

## 💻 Run Locally

### 1. Clone the repository

```powershell
git clone https://github.com/Aryankumavat69/AzureVision-AI.git
```

### 2. Enter the project

```powershell
cd AzureVision-AI
```

### 3. Create virtual environment

```powershell
C:\Python314\python.exe -m venv .venv
```

### 4. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Start the FastAPI server

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

### 6. Open the application

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test the API directly.

---

## 🩺 Health Check

The application includes a health endpoint:

```text
GET /health
```

Example response:

```json
{
    "status": "healthy"
}
```

---

## 🔮 Future Improvements

* ☁️ Azure cloud deployment
* 🔐 Authentication and authorization
* 📊 Image analysis history
* 🗄️ Database integration
* 📱 Improved mobile UI
* 🧠 Additional computer vision models
* 🎯 Object detection
* 📝 Image caption generation
* 📈 Analytics dashboard
* ⚡ Model optimization for cloud deployment
* 🔄 CI/CD pipeline using GitHub Actions

---

## 🎯 Learning Outcomes

This project provides practical experience with:

* Python application development
* Computer Vision
* Machine Learning inference
* Vision Transformers
* Hugging Face Transformers
* PyTorch
* REST APIs
* FastAPI
* Frontend-backend integration
* File upload handling
* JSON APIs
* Cloud deployment concepts
* Azure
* Git and GitHub

---

## 👨‍💻 Author

**Aryan Kumavat**

AI & Data Science Engineering Student

GitHub: `github.com/Aryankumavat69`

---

## ⭐ Project Goal

AzureVision-AI was developed as a practical AI & Data Science project to demonstrate how a machine learning model can be transformed into a usable web application and prepared for cloud deployment.

**From AI Model → API → Web Application → Cloud Deployment 🚀**

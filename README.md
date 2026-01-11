# 🛡️ Insurance Premium Prediction App

A simple **Machine Learning–based Insurance Prediction System** that predicts the **insurance premium category** of a person based on their personal information.  
The project uses a **FastAPI backend**, is **Dockerized**, and is deployed with:

- 🎨 **UI on Hugging Face Spaces**
- ⚙️ **Backend API on Render**

---

## 🚀 Project Overview

This application takes user details such as **age, height, and weight** and predicts the **insurance category** (`Low`, `Medium`, `High`) using a trained Machine Learning model.

### 🔑 Key Features
- ✅ Machine Learning–based prediction
- ✅ FastAPI backend with `/predict` endpoint
- ✅ Dockerized backend service
- ✅ Backend deployed on **Render**
- ✅ Streamlit UI deployed on **Hugging Face Spaces**
- ✅ Clean REST API integration

---

## 🌐 Live Application Links

- **Frontend (UI)**  
  👉 https://huggingface.co/spaces/ruchira01/insurance-prediction  

- **Backend (FastAPI API)**  
  👉 https://insurance-backend-gen1.onrender.com  

---

## 🧠 Machine Learning Model

- Built using **Scikit-learn**
- Trained on insurance-related data
- Predicts insurance **risk category**
- Designed for simplicity and clarity
- Easily extendable to predict actual premium values

---

## 🏗️ System Architecture

User
│
▼
Hugging Face UI (Streamlit)
│
▼
FastAPI Backend (/predict) – Render
│
▼
ML Model → Insurance Category

yaml
Copy code

---

## ⚙️ Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Render

### Frontend
- Streamlit
- Hugging Face Spaces

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

---

## 📡 API Details

### Endpoint
POST /predict

pgsql
Copy code

### Request Body (JSON)
```json
{
  "age": 30,
  "height": 170,
  "weight": 65
}
Response
json
Copy code
{
  "predicted_category": "Medium"
}


🐳 Docker Support

The FastAPI backend is fully Dockerized for easy deployment and portability.

Build Docker Image
docker build -t insurance-prediction-api .

Run Docker Container
docker run -p 8000:8000 insurance-prediction-api

💻 Run Locally
Backend
pip install -r requirements.txt
uvicorn app:app --reload

Frontend
streamlit run app.py

📁 Project Structure
insurance-prediction/
│
├── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md

🔮 Future Enhancements

Add confidence score to predictions

Improve model accuracy with more features

Add database for storing predictions

Authentication & user history

Full cloud deployment (AWS / GCP)
Full cloud deployment (AWS / GCP)

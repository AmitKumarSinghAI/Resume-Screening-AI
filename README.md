# Resume Screening AI 🚀

An AI-powered Resume Screening Application built using Machine Learning, FastAPI, Streamlit, and Docker.

The application predicts the job category of uploaded resumes (PDF/DOCX) using a trained Machine Learning model.

---

# 📌 Features

- Upload Resume (PDF / DOCX)
- Resume Text Extraction
- Resume Preprocessing & Cleaning
- TF-IDF Vectorization
- Machine Learning Prediction
- FastAPI Backend API
- Streamlit Frontend UI
- Dockerized Application
- Cloud Deployment

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## Machine Learning
- Scikit-learn
- TF-IDF Vectorizer

## Deployment
- Docker
- Docker Hub
- Render
- Streamlit Cloud

---

# ⚙️ How It Works

1. User uploads a resume
2. Resume text is extracted
3. Text is cleaned and preprocessed
4. TF-IDF converts text into vectors
5. ML model predicts the job category
6. Prediction is displayed on the screen

---

# 🚀 Deployment

## Backend
- Deployed on Render using Docker

## Frontend
- Deployed on Streamlit Cloud

---

# 🐳 Docker

The backend API is containerized using Docker and pushed to Docker Hub.

---

# 📂 Project Structure

```bash
resume-screening-ai/
│
├── app/
│   ├── main.py
│   ├── model/
│   └── utils/
│
├── frontend/
│   └── app.py
│
├── Dockerfile
├── requirements.txt
└── README.md

🔮 Future Improvements
. Add ATS Resume Score
. Improve Model Accuracy
. Multiple Resume Upload
. Authentication System
. Database Integration

👨‍💻 Author
. Amit Kurmi
. Machine Learning Enthusiast
. Python Developer
. FastAPI & Streamlit Developer
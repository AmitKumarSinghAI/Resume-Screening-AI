# Resume Screening AI & ATS Score 🚀

An AI-powered Resume Screening and ATS Analysis System built using Machine Learning, FastAPI, Streamlit, and Docker.

This application analyzes resumes, predicts the job category, calculates ATS scores, identifies matched and missing skills, and provides resume improvement suggestions based on the uploaded resume and job description.

---

# 📌 Features

- Upload Resume (PDF / DOCX)
- Resume Text Extraction
- Resume Preprocessing & Cleaning
- Job Category Prediction using Machine Learning
- ATS Resume Score Calculation
- Resume & Job Description Matching
- Matched Skills Detection
- Missing Skills Analysis
- Resume Improvement Suggestions
- TF-IDF Vectorization
- Cosine Similarity Matching
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

## Machine Learning & NLP
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- NLP Preprocessing

## Deployment
- Docker
- Docker Hub
- Render
- Streamlit Cloud

---

# ⚙️ How It Works

1. User uploads a resume
2. User pastes the job description
3. Resume text is extracted from PDF/DOCX
4. Resume and job description are cleaned and preprocessed
5. Skills are extracted from both resume and job description
6. TF-IDF converts text into vectors
7. Machine Learning model predicts the job category
8. Cosine similarity calculates resume-job match percentage
9. ATS score is generated
10. Matched and missing skills are identified
11. Resume suggestions are provided to improve the resume

---

# 📊 ATS Features

The system analyzes:

- Resume Match Percentage
- ATS Resume Score
- Matched Skills
- Missing Skills
- Resume Quality
- Education Section
- Experience Section
- Projects Section
- Resume Length
- GitHub & LinkedIn Presence

---

# 🚀 Deployment

## Backend API
- Deployed on Render using Docker

## Frontend
- Deployed on Streamlit Cloud

---

# 🔗 Live Demo

## Frontend
https://resume-screening-ai-4awc7whegzxv3m9snpshar.streamlit.app/

## FastAPI Docs
https://resume-screening-ai-16pz.onrender.com/docs

---

# 🐳 Docker

The backend API is containerized using Docker and pushed to Docker Hub for deployment.

---

# 📂 Project Structure

```bash
resume-screening-ai/
│
├── app/
│   ├── main.py
│   ├── model/
│   ├── utils/
│   └── requirements.txt
│
├── frontend/
│   └── streamlit_app.py
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

# 🔮 Future Improvements

- Add Database Integration
- Add Authentication System
- Add RAG-based Resume Suggestions
- Add AI Career Guidance
- Add Resume Ranking System
- Add Interview Question Generation
- Improve ATS Accuracy
- Multiple Resume Upload Support
- Add Resume Explanation using LLMs
- Add Why This Resume Fits This Role Analysis

---

# 👨‍💻 Author

## Amit Kurmi

- Machine Learning Enthusiast
- Python Developer
- FastAPI & Streamlit Developer
- AI & NLP Learner

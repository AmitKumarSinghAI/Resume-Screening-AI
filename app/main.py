from fastapi import FastAPI, UploadFile, File
import pickle

from app.utils.extract_text import extract_resume_text
from app.utils.preprocess import cleanResume

app = FastAPI()

# Load model
with open("app/model/clf.pkl", "rb") as f:
    model = pickle.load(f)

# Load encoder
with open("app/model/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Load TF-IDF vectorizer
with open("app/model/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)


@app.get("/")
def home():
    return {
        "message": "Resume Screening API Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:
        # Extract text from uploaded PDF
        extracted_text = extract_resume_text(file)

        # Check empty extraction
        if not extracted_text:
            return {
                "error": "No text extracted from resume"
            }

        # Preprocess text
        clean_text = cleanResume(extracted_text)

        # Convert text into TF-IDF vector
        vector = tfidf.transform([clean_text]).toarray()

        # Predict category
        prediction = model.predict(vector)

        # Decode prediction
        predicted_category = encoder.inverse_transform(prediction)

        return {
            "prediction": str(predicted_category[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }
from fastapi import FastAPI, UploadFile, File, Form
import pickle
from sklearn.metrics.pairwise import cosine_similarity

from app.utils.extract_text import extract_resume_text
from app.utils.preprocess import cleanResume
from app.utils.skill import extract_skill

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
async def predict(file: UploadFile = File(...),job_description:str = Form(...)):

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

        # resume skill
        resume_skills = extract_skill(clean_text)

        # Convert text into TF-IDF vector
        vector = tfidf.transform([clean_text]).toarray()

        # preprocess in JD text 
        jd_text = cleanResume(job_description)

        # jd skill
        jd_skills = extract_skill(jd_text)

        # convert JD into vector
        jb_vector = tfidf.transform([jd_text]).toarray()

        # Predict category
        prediction = model.predict(vector)

        # Decode prediction
        predicted_category = encoder.inverse_transform(prediction)

        # Calculate Similarity
        match_score = cosine_similarity(
            vector,
            jb_vector
        )[0][0]

        # Convert to Percentage

        match_percentage = round(
            match_score * 100,
            2
        )

        # match skill
        matched_skills = list(
            set(resume_skills) & set(jd_skills)
        )

        # missing skills
        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )

        # ATS SCORE 

        ats_score = 0

        #skill core
        skill_score = (
            len(matched_skills) /
            max(len(jd_skills),1)
        ) * 40

        ats_score += skill_score

        # Education check
        if "education" in clean_text:
            ats_score+=10

        # Project check
        if "project" in clean_text:
            ats_score+=10

        if "experience" in clean_text:
            ats_score+=10

        # contact info check
        if "gmail.com" in clean_text:
            ats_score+=10
        
        # Resume lenght check
        if len(clean_text.split()) > 300:
            ats_score+=20

        # Final ats_score
        ats_score = round(
            min(ats_score,100),2
        )


        resume_suggestions = []

        # Missing skills suggestion
        if len(missing_skills) > 0:
            resume_suggestions.append(
                "Add missing skills related to the job description."
            )

        # GitHub suggestion
        if "github" not in clean_text:
            resume_suggestions.append(
                "Add GitHub profile link."
            )

        # Linkedin suggestion
        if "linkedin" not in clean_text:
            resume_suggestions.append(
                "Add LinkedIn profile."
            )

        # Reusme lenght suggestion
        if len(clean_text.split()) < 300:
            resume_suggestions.append(
                "Add more project and experience details."
            )
        # project suggestion
        if "project" not in clean_text:
            resume_suggestions.append(
                "Add project section."
            )

        # education sugggestion
        if "education" not in clean_text:
            resume_suggestions.append(
                "Add education section."
            )
            
        # experiecne and achive suggestion
        if "experience" not in clean_text:
            resume_suggestions.append(
                "Add experience and achievements."
            )



        

        return {
            "prediction": str(predicted_category[0]),
            "match_percentage" : float(match_percentage),
            "matched_skills": list(matched_skills),
            "missing_skills": list(missing_skills),
            "ats_score": float(ats_score),
            "resume_suggestions": list(resume_suggestions)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
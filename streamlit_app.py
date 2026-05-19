import streamlit as st
import requests

st.title("Resume Screening APP")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=['pdf', 'docx']
)

job_description = st.text_area(
    "Past Job Description"
)

if uploaded_file is not None:
    if st.button("Predict Category"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                files=files,
                data={
                    "job_description":job_description
                    },
                timeout=360
            )

            if response.status_code == 200:
                result = response.json()

                # st.write("Matched Skills")
                # st.write(result['matched_skills'])

                # st.write("Missing Skills")
                # st.write(result["missing_skills"])

                if "prediction" in result:
                    st.success(f"Predicted Category: {result['prediction']}")

                    if "match_percentage" in result:
                         st.success(f"Resume Match: {result['match_percentage']}%")
                         
                         if "ats_score" in result:
                            st.success(f"ATS Score: {result['ats_score']}")
                else:
                    st.error(f"Unexpected response: {result}")

            else:
                st.error(f"API Error: {response.text}")
      
            st.subheader("Matched Skills")
            st.write(result['matched_skills'])

            st.subheader("Missing Skills")
            st.write(result["missing_skills"])
            
            st.subheader("Resume Suggestions")
            st.write(result["resume_suggestions"])

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
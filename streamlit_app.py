import streamlit as st
import requests

st.title("Resume Screening APP")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=['pdf', 'docx']
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
                "https://resume-screening-ai-16pz.onrender.com/predict",
                files=files,
                timeout=360
            )

            if response.status_code == 200:
                result = response.json()

                if "prediction" in result:
                    st.success(f"Predicted Category: {result['prediction']}")
                else:
                    st.error(f"Unexpected response: {result}")

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
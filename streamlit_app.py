import streamlit as st
import requests

st.title("Resume Screening APP")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type = ['pdf','docx']
)

if uploaded_file is not None:
    if st.button("predict Category"):
        files = {
            "file":(
                uploaded_file.name,
                uploaded_file,
                uploaded_file.type
            )
        }

        response = requests.post(
            "http://127.0.0.1:8000/predict",
             files=files
        )

        result = response.json()

        st.success(
            f"Predicted Category: {result['prediction']}"
        )
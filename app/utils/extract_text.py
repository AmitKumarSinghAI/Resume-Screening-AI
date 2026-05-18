import pdfplumber
from docx import Document
import tempfile
import os


def extract_text_from_pdf(file):

    text = ""

    try:
        with pdfplumber.open(file.file) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + " "

    except Exception as e:
        print("PDF extraction error:", e)

    return text


def extract_text_from_docx(file):

    text = ""

    try:
        doc = Document(file.file)

        for para in doc.paragraphs:

            text += para.text + " "

    except Exception as e:
        print("DOCX extraction error:", e)

    return text


def extract_resume_text(file):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):

        return extract_text_from_docx(file)

    else:

        return "Unsupported file format"
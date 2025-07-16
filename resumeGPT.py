import streamlit as st
import google.generativeai as genAi
import os
import PyPDF2 as pdf
import json

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=''
genAi.configure(api_key=GOOGLE_API_KEY)

#genAi.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Gemini Response Function
def get_gemini_response(resume_text, jd_text):
    input_prompt = f"""
    Hey, act like an experienced ATS (Application Tracking System) evaluator with expertise in tech fields like 
    software engineering, data science, data analytics, and big data engineering. Your job is to evaluate a resume 
    based on the job description provided. The job market is highly competitive, so give your best recommendations 
    for improvement. Assign a percentage match, list missing keywords, and provide a short profile summary.

    Respond in **EXACT** JSON format like:
    {{
        "JD Match": "85%", 
        "MissingKeywords": ["Keyword1", "Keyword2"], 
        "Profile Summary": "..."
    }}

    Resume: {resume_text}
    Job Description: {jd_text}
    """
    
    model = genAi.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_prompt)
    return response.text

# PDF Reader
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

# Streamlit UI
st.set_page_config(page_title="Smart ATS", layout="centered")
st.title("🧠 Smart ATS Resume Checker")
st.markdown("Enhance your resume for **ATS systems** using Gemini AI. Upload your resume and paste the job description.")

# Input section
jd = st.text_area("📄 Paste the Job Description", height=200)
uploaded_file = st.file_uploader("📁 Upload your Resume (PDF format only)", type="pdf")

if st.button("🚀 Submit"):
    if uploaded_file is None or jd.strip() == "":
        st.warning("Please upload your resume and paste the job description.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            resume_text = input_pdf_text(uploaded_file)
            gemini_raw_output = get_gemini_response(resume_text, jd)

        try:
            # Fix JSON string format if needed
            cleaned_output = gemini_raw_output.strip().replace("```json", "").replace("```", "")
            result = json.loads(cleaned_output)

            st.success("✅ Analysis Complete")
            st.markdown(f"### 📊 JD Match Score: **{result['JD Match']}**")

            st.markdown("### ❌ Missing Keywords")
            st.write(result["MissingKeywords"])

            st.markdown("### 🧾 Profile Summary")
            st.write(result["Profile Summary"])

        except Exception as e:
            st.error("⚠️ Failed to parse response. Try again.")
            st.text_area("Raw Gemini Output (for debugging)", gemini_raw_output, height=300)

# ResumeGPT
Check Resume ATS Score with ResumeGPT


---

<h1 align="center" style="font-size: 2.6em; color: #5c67f2;">🧠 Smart ATS Resume Checker</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Python%20App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Gemini%20API-Google%20Generative%20AI-blue?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/Resume%20Parsing-AI%20Insights-green?style=for-the-badge&logo=pdf">
  <img src="https://img.shields.io/badge/ATS%20Tool-Recruitment%20Booster-orange?style=for-the-badge">
</p>

---

## ➤ Project Summary

This project is an intelligent **Applicant Tracking System (ATS)** built with **Streamlit** and powered by **Gemini 1.5 Flash API** from Google. It evaluates a candidate's **resume** against a **job description** and returns:

- ✅ ATS-friendly match percentage  
- ✅ Missing keywords  
- ✅ Profile summary tailored for the JD  

> 🔍 Designed to help job-seekers tailor their resumes for better success in a competitive tech job market.

---

## ➤ Key Features

✔️ Accepts **PDF resume** uploads  
✔️ Accepts **free-form JD** input  
✔️ Analyzes using **Gemini 1.5 Flash LLM**  
✔️ Outputs structured **JSON format** response  
✔️ Returns **match score**, **missing keywords**, and a **custom profile summary**

---

## ➤ How It Works

```plaintext
1. Upload your resume (PDF)
2. Paste the job description
3. Click "Submit"
4. The app sends both inputs to Gemini via a prompt
5. Gemini responds with JSON output
6. Streamlit parses and displays results
````

---

## ➤ Technologies Used

| Component     | Description                           |
| ------------- | ------------------------------------- |
| Streamlit     | Interactive web app UI                |
| Gemini API    | Language model for parsing/responses  |
| PyPDF2        | Reads and extracts resume text        |
| JSON & dotenv | API integration and secure formatting |

---

## ➤ Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-ats-resume-checker.git
cd smart-ats-resume-checker

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

> Don't forget to create a `.env` file and store your API key:

```env
GOOGLE_API_KEY=your_actual_gemini_api_key
```

---

## ➤ Run the App

```bash
streamlit run app.py
```

---

## ➤ Output Example

```json
{
  "JD Match": "85%",
  "MissingKeywords": ["AWS", "CI/CD", "Kubernetes"],
  "Profile Summary": "Experienced Data Scientist with strong Python and ML skills..."
}
```

---

## ➤ Author

**Chirag Kaushik**
*AI + Resume Optimization + Streamlit Wizard*
🔗 [LinkedIn Profile](https://www.linkedin.com/in/chirag-kaushik-profile)

---

## ➤ License

This project is for educational and personal productivity use.
Gemini API by Google is subject to its own [terms of service](https://ai.google.dev/terms).

```


```


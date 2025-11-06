import streamlit as st
import PyPDF2
import io
import random

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(page_title="AI Resume Ranker & Career Coach", page_icon="🧠", layout="wide")

st.title("🧠 AI Resume Ranker & Career Coach")
st.write("Upload your resume and get instant AI-powered insights, feedback, and a ranking score!")

st.markdown("---")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# -----------------------------
# MAIN LOGIC
# -----------------------------
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("📋 Extracted Resume Text Preview:")
    st.text_area("Resume Content", resume_text[:1500] + "...", height=200)
    
    st.markdown("---")
    
    # Simulated ATS Score (placeholder for AI scoring)
    ats_score = random.randint(60, 95)
    st.metric(label="📊 ATS Resume Score", value=f"{ats_score}/100")
    
    # Placeholder AI feedback (to be replaced with Gemini API)
    st.subheader("🧠 AI Feedback & Suggestions")
    st.write("""
    - Add measurable results in your work experience.  
    - Include more action verbs and quantified achievements.  
    - Tailor your resume to specific job roles for a higher ATS match.  
    """)
    
    # Download report
    st.download_button("📥 Download AI Report (Coming Soon)", data="Report generation feature coming soon.", file_name="AI_Resume_Report.txt")
else:
    st.info("👆 Upload a resume file to start analysis.")

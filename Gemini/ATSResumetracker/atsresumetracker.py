import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf

# Streamlit UI Setup
st.set_page_config(page_title="Smart ATS", page_icon="📄", layout="centered")

st.sidebar.title("🔑 API Key Setup")
st.sidebar.write("Get your Google API key [here](https://aistudio.google.com/) and enter it below.")
api_key = st.sidebar.text_input("Enter your API key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    st.sidebar.success("✅ API key entered successfully!")
else:
    st.sidebar.warning("⚠️ Please enter your API key to proceed.")
    st.stop()

def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

st.title("📄 Smart ATS - Resume Evaluator")
st.write("### Optimize your resume for Applicant Tracking Systems (ATS)")

jd = st.text_area("🔍 Paste the Job Description", placeholder="Enter job description here...", height=150)

uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF)", type="pdf", help="Upload a PDF resume for evaluation")

if st.button("🚀 Evaluate Resume"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a resume before submitting.")
    elif not jd.strip():
        st.warning("⚠️ Job description cannot be empty.")
    else:
        with st.spinner("Processing your resume..."):
            resume_text = input_pdf_text(uploaded_file)
            input_prompt = f"""
            Hey, act like a skilled ATS (Applicant Tracking System) with expertise in tech fields.
            Evaluate the resume based on the given job description.
            Consider the competitive job market and provide the best suggestions for improvement.
            Assign a percentage match and identify missing keywords accurately.

            Resume: {resume_text}
            Description: {jd}

            **Response Format:**  
            1. Your resume matches **XX%** of the job description.  
            2. Missing key skills: X, Y, Z.  
            3. Strengths: A, B, C.  
            4. Suggestions for improvement: D, E, F.  
            5. Consider restructuring the resume to emphasize these keywords.  
            """
            response = get_gemini_response(input_prompt)
        
        st.success("✅ Resume evaluation complete!")
        st.subheader("📊 ATS Evaluation Result")
        st.write(response)

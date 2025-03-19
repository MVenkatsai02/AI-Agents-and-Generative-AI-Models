import streamlit as st
import google.generativeai as genai
from io import BytesIO
from docx import Document

# Streamlit App Title
st.title("📝 AI-Powered Resume & Cover Letter Generator")

# Sidebar for API Key
st.sidebar.header("🔑 Enter Your Gemini API Key")
api_key = st.sidebar.text_input("API Key", type="password")
st.sidebar.markdown("[Get your Gemini API key](https://aistudio.google.com/app/apikey)")

if api_key:
    genai.configure(api_key=api_key)
    
    # User Inputs
    st.subheader("📌 Enter Your Details")
    name = st.text_input("Full Name")
    job_title = st.text_input("Job Title")
    experience = st.text_area("Work Experience (Brief Summary)")
    skills = st.text_area("Key Skills (Comma Separated)")
    achievements = st.text_area("Achievements (Optional)")
    cover_letter_prompt = st.text_area("Why are you applying for this job?")
    
    # Select Document Type
    doc_type = st.selectbox("What do you want to generate?", ["Resume", "Cover Letter"])
    
    if st.button("Generate"):  
        with st.spinner("Generating..."):
            prompt = f"""
            Generate a {doc_type.lower()} for:
            Name: {name}
            Job Title: {job_title}
            Experience: {experience}
            Skills: {skills}
            Achievements: {achievements if achievements else 'N/A'}
            Cover Letter Motivation: {cover_letter_prompt if doc_type == 'Cover Letter' else 'N/A'}
            """
            
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                generated_text = response.text
                
                st.success("✅ Generated Successfully!")
                st.text_area("Generated Text", generated_text, height=300)
                
                # Create DOCX File
                doc = Document()
                doc.add_paragraph(generated_text)
                buffer = BytesIO()
                doc.save(buffer)
                buffer.seek(0)
                
                # Download Button
                st.download_button(label="📥 Download as DOCX", data=buffer, file_name=f"{doc_type}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("⚠️ Please enter your API key to proceed.")

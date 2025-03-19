import streamlit as st
import google.generativeai as genai

# Streamlit Page Config
st.set_page_config(page_title="AI Code Refactoring & Optimization Assistant", layout="wide")

# Sidebar for API Key Upload
st.sidebar.header("API Key Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
st.sidebar.markdown("[Get API Key](https://aistudio.google.com/app/apikey)")

# Check API Key
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.sidebar.warning("Please enter your API key to proceed.")
    st.stop()

# Main Page Title
st.title("AI-Powered Code Refactoring & Optimization Assistant")
st.write("Paste your code below, and AI will suggest improvements and optimizations.")

# Code Input
code_input = st.text_area("Enter your code:", height=300)

# Process Code on Button Click
if st.button("Optimize Code"):
    if code_input.strip():
        with st.spinner("Refactoring and optimizing your code..."):
            try:
                prompt = f"Refactor and optimize the following code with best practices, readability, and efficiency in mind:\n\n{code_input}"
                response = model.generate_content(prompt)
                optimized_code = response.text
                
                st.subheader("Optimized Code:")
                st.code(optimized_code, language="python")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some code before optimizing.")

import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.set_page_config(page_title="Multi-Language Code Assistant", layout="wide")
st.title("💡 Multi-Language Code Assistant")

# Sidebar for API Key
st.sidebar.header("🔑 API Key Configuration")
st.sidebar.write("Get your API key from [Google AI Studio](https://aistudio.google.com/)")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

# Function to get response from Gemini 1.5 Flash
def get_gemini_response(prompt, api_key):
    if not api_key:
        return "Error: API key is required."
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text

# User input for query
query = st.text_area("Enter your programming question or request:")

# Select programming language
languages = ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "Swift", "Kotlin", "PHP", "Ruby"]
language = st.selectbox("Select Programming Language:", languages)

# Generate response
if st.button("Generate Code"):
    if query and api_key:
        prompt = f"Write a {language} code snippet for: {query}"
        response = get_gemini_response(prompt, api_key)
        
        st.subheader("Generated Code:")
        st.code(response, language=language.lower())
    else:
        st.warning("Please enter both an API key and a query before generating code.")

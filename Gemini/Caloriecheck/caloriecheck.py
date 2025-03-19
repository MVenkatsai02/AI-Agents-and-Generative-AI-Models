import streamlit as st
import google.generativeai as genai
from PIL import Image

def get_gemini_response(input_text, image, prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    return None

st.set_page_config(page_title="Calorie Checker", page_icon="🍎", layout="centered")

st.sidebar.title("🔑 API Key Setup")
st.sidebar.write("To use this app, upload your Google Gemini API key.")
st.sidebar.markdown("[Get your API key here](https://aistudio.google.com/)")
api_key = st.sidebar.text_input("Enter your API Key:", type="password")

st.markdown(
    """
    <h1 style="text-align:center;">🍎 Calorie Checker</h1>
    <p style="text-align:center; color:gray;">Analyze food items in an image and get total calorie details.</p>
    <hr>
    """, 
    unsafe_allow_html=True
)

st.subheader("📌 Enter Details")
input_text = st.text_input("Enter additional context (optional):", placeholder="E.g., Is this a healthy meal?")
uploaded_file = st.file_uploader("📷 Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("🍽️ Analyze Calories", use_container_width=True)

input_prompt = """
You are an expert nutritionist. Analyze the food items from the image and calculate the total calories.
Provide detailed calorie breakdown in the following format:

🍽️ **Calorie Breakdown**  
1. Item Name - Calories  
2. Item Name - Calories  
...
"""

if submit:
    if not api_key:
        st.error("⚠️ Please enter your API key in the sidebar before proceeding!")
    elif uploaded_file is None:
        st.error("⚠️ Please upload a food image before analyzing!")
    else:
        with st.spinner("Analyzing food items... 🔄"):
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_text, image_data, input_prompt, api_key)
        st.success("✅ Analysis Complete!")
        st.subheader("📊 Results")
        st.markdown(response, unsafe_allow_html=True)

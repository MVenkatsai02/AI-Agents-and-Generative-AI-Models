import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="🍽️ AI Cooking Assistant", layout="wide")

# Sidebar for API Key Upload
st.sidebar.title("🔑 Upload API Key")
st.sidebar.markdown("""
- [Get Google Gemini API Key](https://aistudio.google.com/app/apikey)  
""")

# API Key Input
gemini_api_key = st.sidebar.text_input("Google Gemini API Key", type="password")

# Ensure API key is provided
if not gemini_api_key:
    st.sidebar.warning("Please enter your API key to proceed.")
    st.stop()

# Initialize Gemini API
genai.configure(api_key=gemini_api_key)

# Streamlit App Main Interface
st.title("🍽️ Multimodal AI Cooking Assistant")
st.subheader("Get AI-powered recipe suggestions, cooking techniques, and meal ideas!")

# User Inputs
cuisine = st.selectbox("Select Cuisine:", ["Italian", "Indian", "Chinese", "Mexican", "French", "Mediterranean"])
meal_type = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert"])
dietary_preference = st.selectbox("Dietary Preference:", ["None", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo"])
upload_image = st.file_uploader("📷 Upload an Image of Ingredients (Optional)", type=["jpg", "png", "jpeg"])
custom_ingredients = st.text_area("Or Enter Ingredients Manually (comma-separated):", "Tomatoes, Garlic, Basil, Cheese")

# Function to process image for AI input
def encode_image(image_file):
    image = Image.open(image_file)
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

# Function to generate recipe
def generate_recipe(cuisine, meal_type, dietary_preference, ingredients, image_data=None):
    prompt = f"""
    Generate a {cuisine} recipe for {meal_type} that is {dietary_preference.lower() if dietary_preference != 'None' else 'regular'}.
    Ingredients: {ingredients}
    Provide:
    - A detailed step-by-step cooking method
    - Cooking time, servings, and nutritional information
    - Optional variations or ingredient substitutions
    {"Use the uploaded image to refine the recipe suggestions." if image_data else ""}
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Handle multimodal input (text + image)
    if image_data:
        response = model.generate_content([prompt, image_data])
    else:
        response = model.generate_content(prompt)
    
    return response.text if response else "Sorry, I couldn't generate the recipe."

# Generate Recipe
if st.button("Generate Recipe"):
    with st.spinner("Generating recipe..."):
        image_data = encode_image(upload_image) if upload_image else None
        recipe_text = generate_recipe(cuisine, meal_type, dietary_preference, custom_ingredients, image_data)
    
    # Display Recipe
    st.subheader("📜 AI-Generated Recipe")
    st.write(recipe_text)

    # Download Recipe as Text File
    st.download_button(
        label="📥 Download Recipe",
        data=recipe_text,
        file_name=f"{meal_type}_{cuisine}_recipe.txt",
        mime="text/plain",
    )



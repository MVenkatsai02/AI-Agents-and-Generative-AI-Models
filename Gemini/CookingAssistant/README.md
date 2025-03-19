# 🍽️ AI Cooking Assistant

## Description
The **AI Cooking Assistant** is a multimodal application powered by Google Gemini AI that generates customized recipes based on user preferences. Users can select a cuisine, meal type, and dietary preference while optionally uploading an image of ingredients or manually entering them. The AI then provides a detailed recipe with step-by-step instructions, cooking time, servings, and nutritional information.

## Features
- 📌 **Cuisine Selection:** Choose from various cuisines like Italian, Indian, Chinese, Mexican, French, and Mediterranean.
- 🍽️ **Meal Type:** Get recipes for Breakfast, Lunch, Dinner, Snacks, and Desserts.
- 🥗 **Dietary Preferences:** Supports Vegetarian, Vegan, Gluten-Free, Keto, and Paleo diets.
- 📷 **Ingredient Image Recognition:** Upload an image of ingredients for AI-enhanced recipe suggestions.
- ✍️ **Manual Ingredients Input:** Enter ingredients manually if no image is provided.
- ⏳ **Step-by-Step Cooking Guide:** AI provides detailed instructions, cooking time, and nutritional details.
- 📥 **Download Recipe Feature:** Save your recipe as a text file for later use.

## Requirements
- Python 3.8+
- Required Libraries:
  - `streamlit`
  - `google-generativeai`
  - `Pillow`
  - `io`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-cooking-assistant.git
   cd ai-cooking-assistant
   ```
2. Install dependencies:
   ```sh
   pip install streamlit google-generativeai Pillow
   ```

## Usage
1. Obtain a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Run the application:
   ```sh
   streamlit run app.py
   ```
3. Enter your API key in the sidebar.
4. Select cuisine, meal type, and dietary preference.
5. Upload an image of ingredients or enter them manually.
6. Click **Generate Recipe** to receive an AI-powered cooking guide.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Powered by **Google Gemini AI** for natural language and image analysis.
- Built with **Streamlit** for an interactive UI.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀
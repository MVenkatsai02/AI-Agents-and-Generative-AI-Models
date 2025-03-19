# 🍎 Calorie Checker

## Overview
The **Calorie Checker** is an AI-powered web app that analyzes food items from an uploaded image and provides a detailed calorie breakdown. It leverages Google Gemini AI to extract nutritional information based on the detected food items.

## Features
- 📸 **Image Upload**: Users can upload an image of their meal.
- 🔎 **Calorie Analysis**: AI provides a detailed calorie breakdown for each food item.
- ✨ **Additional Context**: Users can add custom prompts (e.g., "Is this a healthy meal?").
- ✅ **Easy-to-Use Interface**: Built using **Streamlit** for a seamless experience.

## Prerequisites
- Python 3.8+
- A Google Gemini API key ([Get your API key here](https://aistudio.google.com/))

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/calorie-checker.git
   cd calorie-checker
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
1. Export or set up your Google Gemini API key:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"  # On Windows: set GEMINI_API_KEY=your_api_key_here
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided local URL in your browser.

## Usage
1. Enter an optional **context** (e.g., "Is this a healthy meal?").
2. Upload a **food image** (JPG, JPEG, or PNG).
3. Click **"Analyze Calories"**.
4. View the **detailed calorie breakdown**.

## Deployment
To deploy on **Streamlit Cloud**, follow these steps:
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and deploy your repository.
3. Set your `GEMINI_API_KEY` as an environment variable.

Alternatively, you can deploy using **Docker**:
```bash
docker build -t calorie-checker .
docker run -p 8501:8501 calorie-checker
```

## Troubleshooting
- **Invalid API Key**: Ensure you entered the correct Google Gemini API key.
- **Image Not Processed**: Try re-uploading the image in JPG or PNG format.
- **Slow Response**: AI processing times depend on the server load.

## License
This project is licensed under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀


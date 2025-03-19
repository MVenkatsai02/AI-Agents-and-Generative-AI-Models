# 📄 Smart ATS - Resume Evaluator

An AI-powered tool that evaluates resumes against job descriptions using Google Gemini AI. It extracts text from PDF resumes, compares it with job descriptions, and provides insights into keyword match percentage, missing skills, strengths, and improvement suggestions.

## 🚀 Features

✅ AI-driven ATS-based resume evaluation  
✅ Extracts text from PDF resumes  
✅ Compares resumes with job descriptions  
✅ Identifies missing keywords and areas of improvement  
✅ Provides a percentage match score  
✅ Interactive Streamlit UI  

## 📂 Project Structure

```bash
smart-ats/
├── app.py               # Main Streamlit application
├── requirements.txt     # List of dependencies
├── README.md            # Documentation
└── .gitignore           # Ignore unnecessary files
```

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MVenkatsai02/AI-Agents-and-Generative-AI-Models/tree/main/Gemini/ATSResumetracker
cd smart-ats
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🖥️ Running Locally

### 🔹 Start Streamlit Application
```bash
streamlit run app.py
```
Your UI will be available at:  
👉 http://localhost:8501

## 🌍 Deployment

### Deploy on Streamlit Cloud
1️⃣ Push the project to GitHub.  
2️⃣ Go to Streamlit Cloud → Click "Deploy an App".  
3️⃣ Select the GitHub repository → Set main file path to `app.py`.  
4️⃣ Deploy and share your app link.  

## 📌 Example Usage

1️⃣ Open the Streamlit UI.  
2️⃣ Enter a job description in the provided text area.  
3️⃣ Upload your resume in PDF format.  
4️⃣ Click **Evaluate Resume**.  
5️⃣ View AI-generated feedback, including ATS match percentage, missing keywords, and improvement suggestions.

## 🔧 Troubleshooting

💡 **Issue: API Key Not Found**  
✔️ Ensure you enter a valid Google Gemini API key in the sidebar.  
✔️ Get your API key from [Google AI Studio](https://aistudio.google.com/).  
✔️ Restart the Streamlit app after updating the API key.  

💡 **Issue: Dependencies Missing**  
✔️ Run `pip install -r requirements.txt`.  
✔️ Ensure the virtual environment is activated.

## 🛡️ License

This project is open-source under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!  
🔹 Found a bug? Create an issue on GitHub.  
🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com  

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀


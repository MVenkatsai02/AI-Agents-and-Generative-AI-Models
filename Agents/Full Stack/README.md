# 🚀 Multi-Agent AI Code Generator

An AI-powered multi-agent system that generates professional frontend and backend code, along with optimized Dockerfiles, based on user-provided project requirements. Built using Streamlit and powered by Gemini AI models.


## 🛠️ Features

✅ AI-generated backend code (Node.js, Django, Flask, FastAPI, Spring Boot, Laravel, etc.) 

✅ AI-generated frontend code (React, Vue, Angular, Svelte, HTML, CSS, JavaScript, TypeScript) 

✅ AI-generated Dockerfiles for both frontend and backend 

✅ Ensures scalability, security, and clean architecture

✅ Streamlit UI for an interactive experience 

## 📂 Project Structure

```bash
multi-agent-code-generator/
├── app.py                 # Main Streamlit application
├── .env                   # API key storage (not to be committed)
├── requirements.txt       # List of dependencies
├── README.md              # Documentation
└── .gitignore             # Ignore unnecessary files
```

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MVenkatsai02/AI-Agents-and-Generative-AI-Models/tree/main/Agents/Full Stack
cd multi-agent-ai-code-generator
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

### 4️⃣ Deploy on Streamlit Cloud

Push the project to GitHub.
Go to Streamlit Cloud → Click "Deploy an App".
Select GitHub repo → Set main file path to `app.py`.
Deploy and share your app link.

## 📌 Example Usage

1️⃣ Open the Streamlit UI.

2️⃣ Enter your project requirements.

3️⃣ Click **Generate Code**.

4️⃣ View the AI-generated frontend & backend code along with Dockerfiles.

## 🔧 Troubleshooting

💡 **Issue: API Key Not Found**
✔️ Ensure `.env` file contains `GOOGLE_API_KEY=your_api_key_here`.
✔️ Restart the Streamlit app after updating the `.env` file.

💡 **Issue: Missing Dependencies**
✔️ Run `pip install -r requirements.txt`.
✔️ Ensure virtual environment is activated.

## 🛡️ License

This project is open-source under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀


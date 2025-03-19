# Multi-Language Code Assistant

## 📌 Overview
The **Multi-Language Code Assistant** is a Streamlit-based web application that leverages Google's **Gemini 1.5 Flash** model to generate programming code snippets based on user queries. Users can input a programming-related question, select their preferred language, and receive AI-generated code.

## 🚀 Features
- Supports multiple programming languages including **Python, JavaScript, Java, C++, C#, Go, Rust, Swift, Kotlin, PHP, and Ruby**.
- Integrates **Google Gemini AI** for high-quality code generation.
- Simple and interactive **Streamlit UI**.
- Secure API key input for authentication.

## 🛠️ Installation & Setup
### 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed, then run the following command:
```bash
pip install streamlit google-generativeai
```

### 2️⃣ Get a Google Gemini API Key
- Visit [Google AI Studio](https://aistudio.google.com/)
- Generate an API key
- Copy the key for use in the application

### 3️⃣ Run the Application
Save the script as `app.py` and run:
```bash
streamlit run app.py
```

## 🔑 API Key Setup
- Enter your **Google Gemini API key** in the sidebar to enable AI-powered code generation.
- The API key is required to interact with the Gemini model.

## 🖥️ How to Use
1. Enter a programming-related **question or request** in the text area.
2. Select a **programming language** from the dropdown menu.
3. Click on **"Generate Code"** to receive an AI-generated code snippet.

## 🎯 Example Usage
### Input:
- **Query:** "Write a function to check if a number is prime"
- **Language:** Python

### Output:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## 📝 Notes
- Ensure you have a **valid API key** before generating code.
- The generated code should be reviewed and tested before use in production.

## 📜 License
This project is open-source and free to use under the **MIT License**.

## 🤝 Contributing
Feel free to submit issues or feature requests on the **GitHub repository** (if applicable).

## 📩 Contact 

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

---
💡 Happy Coding! 🚀


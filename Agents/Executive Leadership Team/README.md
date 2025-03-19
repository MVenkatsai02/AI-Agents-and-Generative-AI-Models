# AI Executive Leadership Team

## Overview
The **AI Executive Leadership Team** is a Streamlit-based application that leverages AI-powered executive roles to provide strategic insights on business ideas, challenges, and decisions. Each virtual executive agent specializes in a different domain to deliver comprehensive analysis and guidance.

## Features
- **Multi-Agent System**: AI-powered executive roles (CEO, CFO, COO, CMO, CTO, CHRO) analyze business input.
- **Business Strategy Analysis**: Provides insights on leadership, finance, operations, marketing, technology, and HR.
- **Streamlit-Based UI**: Simple and interactive user interface for easy input and results visualization.
- **Google Gemini AI Integration**: Uses the `Gemini-1.5-flash` model to generate responses.

## Installation
To run this application, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/ai-executive-leadership.git
cd ai-executive-leadership
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

## Usage
1. **Enter Business Challenge or Idea**: Provide a description of your business idea, challenge, or decision.
2. **Enter Google Gemini API Key**: Add your API key in the sidebar.
3. **Click 'Get Executive Insights'**: AI agents will analyze your input and provide detailed feedback.
4. **View Responses**: Insights from different executive roles will be displayed on the screen.

## AI Executive Roles
- **CEO (Chief Executive Officer)**: Provides high-level business strategy and vision.
- **CFO (Chief Financial Officer)**: Analyzes financial feasibility and risk management.
- **COO (Chief Operating Officer)**: Assesses operational efficiency and execution strategies.
- **CMO (Chief Marketing Officer)**: Develops marketing and branding recommendations.
- **CTO (Chief Technology Officer)**: Evaluates technical infrastructure and innovation.
- **CHRO (Chief Human Resources Officer)**: Advises on hiring, talent management, and HR challenges.

## API Key
To use the Google Gemini AI, you need an API key. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and enter it in the sidebar.

## Requirements
- Python 3.8+
- Streamlit
- `agno` package (for AI agents)
- `google.generativeai` (for Gemini API integration)

## Troubleshooting
If you encounter issues:
- Ensure you have a valid Google Gemini API key.
- Check that all dependencies are installed.
- Restart the Streamlit app (`Ctrl + C` and run `streamlit run app.py` again).

## License
This project is open-source under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com


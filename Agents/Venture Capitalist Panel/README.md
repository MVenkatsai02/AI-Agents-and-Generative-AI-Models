# AI Venture Capitalist Panel 💰

## Overview
The **AI Venture Capitalist Panel** is a Streamlit-based application that provides AI-powered startup evaluations. This tool simulates a panel of expert venture capitalists (VCs) to assess your business idea, market potential, financial viability, technical feasibility, and growth strategies.

## Features
- **Serial Entrepreneur VC** – Evaluates startup feasibility and execution.
- **Market Analyst VC** – Assesses market trends, competition, and demand.
- **Financial Expert VC** – Analyzes financial risks, fundraising strategies, and potential returns.
- **Tech Advisor VC** – Reviews the Minimum Viable Product (MVP) for technical feasibility.
- **Growth Strategist VC** – Provides scaling and go-to-market insights.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip
- Streamlit
- `agno` library

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/ai-vc-panel.git
   cd ai-vc-panel
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Obtain your Google AI GEMINI API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Enter the API key in the sidebar input field.
3. Provide details about your startup:
   - Business idea
   - Funding required (in USD)
   - MVP description
4. Click **Get VC Feedback** to receive insights from AI-powered VCs.

## Dependencies
- `streamlit` – For UI and user interaction.
- `agno.agent` – For creating AI-driven VC agents.
- `agno.models.google` – For integrating Google's Gemini AI model.
- `logging` – For debugging and logging errors.

## Example Output
Upon submitting your startup details, the app provides structured feedback from five AI VC agents covering execution, market potential, financial aspects, technology feasibility, and scaling strategies.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com


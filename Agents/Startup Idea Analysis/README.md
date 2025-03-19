# Startup Idea Analysis Agent 📈

## Overview
The **Startup Idea Analysis Agent** is a Streamlit-based AI-powered application that helps users analyze emerging trends and startup opportunities based on their topics of interest. It leverages multiple AI agents to collect news, summarize articles, and extract meaningful insights using the **Agno framework** and **Gemini AI model**.

## Features
- **Real-time Web Search**: Uses **DuckDuckGo** to collect the latest news articles on the given topic.
- **AI-Powered Summarization**: Extracts key insights from collected articles.
- **Trend Analysis**: Identifies emerging trends and potential startup opportunities.
- **Multi-Agent Collaboration**: A team of AI agents works together to generate a detailed analysis report.
- **User-Friendly Interface**: Simple Streamlit UI for easy interaction.

## How It Works
1. **User Input**: Enter a startup idea or topic of interest.
2. **News Collection**: The **News Collector Agent** fetches the latest articles on the topic using **DuckDuckGo**.
3. **Article Summarization**: The **Summary Writer Agent** processes and summarizes the collected articles.
4. **Trend Analysis**: The **Trend Analyzer Agent** extracts insights and identifies startup opportunities.
5. **Final Report**: The AI generates a detailed report, providing valuable insights to entrepreneurs.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.8 or later).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/startup-idea-analysis-agent.git
   cd startup-idea-analysis-agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Configuration
- Enter your **Gemini API Key** in the sidebar when running the app.
- Provide a startup idea or topic to analyze trends.

## Tech Stack
- **Streamlit** - Web UI
- **Agno Framework** - AI Agent Orchestration
- **DuckDuckGo API** - Web Search
- **Newspaper4k** - Article Summarization
- **Google Gemini AI** - AI Model for NLP tasks

## Example Usage
1. **Enter a startup idea**, e.g., `AI-powered healthcare assistant`.
2. **Click 'Generate Analysis'**.
3. **Wait for AI processing**.
4. **View the trend analysis report**, including startup opportunities, emerging trends, and challenges.

## Future Improvements
- Support for additional news sources.
- More in-depth financial and market analysis.
- Integration with real-time social media trend monitoring.



## License
This project is licensed under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com
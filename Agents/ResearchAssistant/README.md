# AI-Powered Research Assistant

## Overview
This AI-powered research assistant leverages multi-agent collaboration to fetch, analyze, and summarize research papers from various sources, including the web and arXiv. It is built using Streamlit and integrates Google's Gemini AI model along with web and academic research tools.

## Features
- **Web Research Agent**: Searches the web for relevant information and extracts key points with citations.
- **arXiv Research Agent**: Retrieves the most relevant academic papers from arXiv and summarizes them.
- **Summarization Agent**: Condenses research findings into concise, well-structured summaries.
- **Multi-Agent Collaboration**: A team of AI agents working together to ensure accurate citations and comprehensive research summaries.

## Technologies Used
- **Streamlit**: For interactive UI
- **Google Gemini API**: AI model for natural language understanding
- **DuckDuckGoTools**: Web search integration
- **ArxivTools**: Academic paper retrieval
- **Python**: Primary programming language

## Installation
### Prerequisites
- Python 3.8+
- A valid [Gemini API Key](https://ai.google.dev/)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-research-assistant.git
   cd ai-research-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter your **Gemini API Key** in the sidebar.
2. Input a research topic in the provided text box.
3. Click **Fetch and Summarize** to retrieve and summarize research findings.
4. View the structured research summary directly in the app.

## Example Output
```
## Research Summary
- **Paper 1:** Title - "Deep Learning in AI" (arXiv:2301.12345)
  - Summary: Discusses the advancements in deep learning for AI applications.
  - Citation: Author et al., 2023

- **Web Search Insights:**
  - AI has seen rapid development in recent years, impacting multiple fields.
  - Key challenges include data bias and computational cost.
```

## License
This project is licensed under the MIT License.


## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀

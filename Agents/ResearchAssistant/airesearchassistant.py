import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Streamlit UI
st.sidebar.title("API Key Setup")
st.sidebar.write("[Get your Gemini API key here](https://ai.google.dev/)")
api_key = st.sidebar.text_input("Enter your API Key", type="password")

if not api_key:
    st.warning("Please enter your API key to proceed.")
    st.stop()

# Web Research Agent
web_research_agent = Agent(
    name="Web Research Agent",
    role="Fetch relevant research information from the web",
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key),
    tools=[DuckDuckGoTools()],
    instructions="Always provide citations and extract key points from sources.",
    markdown=True,
)

# arXiv Research Agent
arxiv_agent = Agent(
    name="arXiv Agent",
    role="Fetch academic papers from arXiv",
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key),
    tools=[ArxivTools()],
    instructions="Retrieve the most relevant papers, summarize them, and extract citations.",
    markdown=True,
)

# Summarization Agent
summarization_agent = Agent(
    name="Summarization Agent",
    role="Summarize research papers and key findings",
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key),
    instructions="Generate concise and informative summaries while retaining key details and citations.",
    markdown=True,
)

# Multi-Agent Team
research_team = Agent(
    team=[web_research_agent, arxiv_agent, summarization_agent],
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key),
    instructions=["Ensure accuracy of citations", "Provide structured summaries"],
    markdown=True,
)

# Streamlit UI
topic = st.text_input("Enter research topic:")
if st.button("Fetch and Summarize"):
    if topic:
        st.write("## Research Summary")
        response = research_team.run(f"Find and summarize research papers on {topic}")
        st.markdown(response.content)
    else:
        st.warning("Please enter a research topic.")

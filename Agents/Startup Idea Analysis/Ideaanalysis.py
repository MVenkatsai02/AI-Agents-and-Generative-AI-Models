import streamlit as st
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.google import Gemini
from agno.tools.newspaper4k import Newspaper4kTools
import logging

logging.basicConfig(level=logging.DEBUG)

# Setting up Streamlit app
st.title("Startup Idea Analysis Agent 📈")
st.caption("Get the latest trend analysis and startup opportunities based on your topic of interest in a click!.")

topic = st.text_input("Enter the Startup Idea of your intrest:")
Google_api_key = st.sidebar.text_input("Enter GEMINI API Key", type="password")

if st.button("Generate Analysis"):
    if not Google_api_key:
        st.warning("Please enter the required API key.")
    else:
        with st.spinner("Processing your request..."):
            try:
                # Initialize GEMINI model
                model=Gemini(id="gemini-1.5-flash", api_key=Google_api_key)

                # Define News Collector Agent - Duckduckgo_search tool enables an Agent to search the web for information.
                search_tool = DuckDuckGoTools(search=True, news=True, fixed_max_results=5)
                news_collector = Agent(
                    name="News Collector",
                    role="Collects recent news articles on the given topic",
                    tools=[search_tool],
                    model=model,
                    instructions=["Gather latest articles on the topic"],
                    show_tool_calls=True,
                    markdown=True,
                )

                # Define Summary Writer Agent
                news_tool = Newspaper4kTools(read_article=True, include_summary=True)
                summary_writer = Agent(
                    name="Summary Writer",
                    role="Summarizes collected news articles",
                    tools=[news_tool],
                    model=model,
                    instructions=["Provide concise summaries of the articles"],
                    show_tool_calls=True,
                    markdown=True,
                )

                # Define Trend Analyzer Agent
                trend_analyzer = Agent(
                    name="Trend Analyzer",
                    role="Analyzes trends from summaries",
                    model=model,
                    instructions=["Identify emerging trends and Startup opportunities on the topic"],
                    show_tool_calls=True,
                    markdown=True,
                )

                # The multi agent Team setup of Agno:
                agent_team = Agent(
                    team=[news_collector, summary_writer, trend_analyzer],
                    instructions=[
                        "First, search DuckDuckGo for recent news articles related to the user's specified topic.",
                        "Then, provide the collected article links to the summary writer.",
                        "Important: you must ensure that the summary writer receives all the article links to read.",
                        "Next, the summary writer will read the articles and prepare concise summaries of each.",
                        "After summarizing, the summaries will be passed to the trend analyzer.",
                        "Finally, the trend analyzer will identify emerging trends and potential startup opportunities based on the summaries provided in a detailed Report form so that any young entreprenur can get insane value reading this easily"
                    ],
                    show_tool_calls=True,
                    markdown=True,
                )

                # Executing the workflow
                # Step 1: Collect news
                news_response = news_collector.run(f"Collect recent news on {topic}")
                articles = news_response.content

                # Step 2: Summarize articles
                summary_response = summary_writer.run(f"Summarize the following articles:\n{articles}")
                summaries = summary_response.content

                # Step 3: Analyze trends
                trend_response = trend_analyzer.run(f"Analyze trends from the following summaries:\n{summaries}")
                analysis = trend_response.content

                st.subheader("Trend Analysis and Potential Opportunities on the Startup Idea")
                st.write(analysis)

            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Enter the topic and API keys, then click 'Generate Analysis' to start.")
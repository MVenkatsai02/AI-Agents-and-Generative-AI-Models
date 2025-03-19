import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
import logging

logging.basicConfig(level=logging.DEBUG)

st.title("AI Executive Leadership Team 🏢")
st.caption("Get strategic insights from AI-powered executive roles.")

# User input for business query
business_input = st.text_area("Enter your business idea, challenge, or decision:")
Google_api_key = st.sidebar.text_input("Enter GEMINI API Key", type="password")

if st.button("Get Executive Insights"):
    if not Google_api_key:
        st.warning("Please enter the required API key.")
    else:
        with st.spinner("Processing your request..."):
            try:
                # Initialize GEMINI model
                model = Gemini(id="gemini-1.5-flash", api_key=Google_api_key)

                # Define Executive Agents
                ceo_agent = Agent(
                    name="CEO",
                    role="Provides strategic vision and leadership",
                    model=model,
                    instructions=["Analyze the input from a high-level business strategy perspective and provide recommendations."],
                    markdown=True,
                )

                cfo_agent = Agent(
                    name="CFO",
                    role="Manages financial strategy and risks",
                    model=model,
                    instructions=["Evaluate financial risks, budgeting needs, and financial feasibility of the input."]
                )

                coo_agent = Agent(
                    name="COO",
                    role="Oversees operations and logistics",
                    model=model,
                    instructions=["Assess operational feasibility, supply chain needs, and execution strategies."]
                )

                cmo_agent = Agent(
                    name="CMO",
                    role="Leads marketing and branding",
                    model=model,
                    instructions=["Develop a marketing and branding strategy based on the input."]
                )

                cto_agent = Agent(
                    name="CTO",
                    role="Manages technology and innovation",
                    model=model,
                    instructions=["Analyze technical requirements, infrastructure, and innovation opportunities."]
                )

                chro_agent = Agent(
                    name="CHRO",
                    role="Oversees human resources and talent management",
                    model=model,
                    instructions=["Identify hiring needs, talent management strategies, and HR challenges."]
                )

                # Multi-agent workflow
                executive_team = Agent(
                    team=[ceo_agent, cfo_agent, coo_agent, cmo_agent, cto_agent, chro_agent],
                    instructions=[
                        "Each executive agent will analyze the input from their department's perspective.",
                        "Each agent will provide insights, conclusions, and improvement suggestions.",
                        "Finally, compile a comprehensive strategic report."
                    ],
                    markdown=True,
                )

                # Step 1: Gather insights from each executive
                ceo_response = ceo_agent.run(business_input).content
                cfo_response = cfo_agent.run(business_input).content
                coo_response = coo_agent.run(business_input).content
                cmo_response = cmo_agent.run(business_input).content
                cto_response = cto_agent.run(business_input).content
                chro_response = chro_agent.run(business_input).content

                # Display responses
                st.subheader("Executive Leadership Insights")
                st.write("### CEO (Strategic Vision)")
                st.write(ceo_response)
                st.write("### CFO (Financial Analysis)")
                st.write(cfo_response)
                st.write("### COO (Operational Strategy)")
                st.write(coo_response)
                st.write("### CMO (Marketing Strategy)")
                st.write(cmo_response)
                st.write("### CTO (Technology & Innovation)")
                st.write(cto_response)
                st.write("### CHRO (HR & Talent Management)")
                st.write(chro_response)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Enter a business challenge or idea and API key, then click 'Get Executive Insights' to start.")

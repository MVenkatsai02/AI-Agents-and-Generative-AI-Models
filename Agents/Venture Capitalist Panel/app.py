import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
import logging

logging.basicConfig(level=logging.DEBUG)

st.title("AI Venture Capitalist Panel 💰")
st.caption("Get expert startup evaluation from AI-powered VCs.")

# Sidebar with instructions and API key input
st.sidebar.title("Instructions")
st.sidebar.write("1. Obtain your API key from Google AI Studio.")  
st.sidebar.write("2. Click the link below to get your API key:")  
st.sidebar.markdown("[Get API Key](https://aistudio.google.com/app/apikey)", unsafe_allow_html=True)  
st.sidebar.write("3. Enter the API key in the field below.")  
st.sidebar.write("4. Fill in your startup details and get AI-driven VC insights.")  
Google_api_key = st.sidebar.text_input("Enter GEMINI API Key", type="password")

# User inputs
business_idea = st.text_area("Enter your startup idea:")
funding_required = st.number_input("Enter the amount you want to raise (in USD):", min_value=1000)
mvp_description = st.text_area("Describe your Minimum Viable Product (MVP):")

if st.button("Get VC Feedback"):
    if not Google_api_key:
        st.warning("Please enter the required API key.")
    else:
        with st.spinner("Processing your request..."):
            try:
                # Initialize GEMINI model
                model = Gemini(id="gemini-1.5-flash", api_key=Google_api_key)

                # Define VC Agents
                serial_entrepreneur = Agent(
                    name="Serial Entrepreneur VC",
                    role="Evaluates startup feasibility and execution",
                    model=model,
                    instructions=["Analyze the business idea based on real-world startup execution experience and viability."]
                )

                market_analyst = Agent(
                    name="Market Analyst VC",
                    role="Assesses market potential and competition",
                    model=model,
                    instructions=["Evaluate market trends, competition, and demand for the given business idea."]
                )

                financial_expert = Agent(
                    name="Financial Expert VC",
                    role="Analyzes financial viability and fundraising strategy",
                    model=model,
                    instructions=["Assess financial risks, potential returns, and the feasibility of raising the specified funding amount."]
                )

                tech_advisor = Agent(
                    name="Tech Advisor VC",
                    role="Reviews the MVP’s technical feasibility",
                    model=model,
                    instructions=["Evaluate the MVP’s technology stack, scalability, and innovation potential."]
                )

                growth_strategist = Agent(
                    name="Growth Strategist VC",
                    role="Provides scaling and go-to-market insights",
                    model=model,
                    instructions=["Suggest strategies for scaling, user acquisition, and go-to-market execution."]
                )

                # Gather responses from VC agents
                entrepreneur_response = serial_entrepreneur.run(business_idea).content
                market_response = market_analyst.run(business_idea).content
                finance_response = financial_expert.run(f"{business_idea}, Funding Required: {funding_required}").content
                tech_response = tech_advisor.run(mvp_description).content
                growth_response = growth_strategist.run(business_idea).content

                # Display responses
                st.subheader("VC Panel Insights")
                st.write("### Serial Entrepreneur VC (Startup Execution)")
                st.write(entrepreneur_response)
                st.write("### Market Analyst VC (Market & Competition)")
                st.write(market_response)
                st.write("### Financial Expert VC (Fundraising & Risks)")
                st.write(finance_response)
                st.write("### Tech Advisor VC (MVP Review)")
                st.write(tech_response)
                st.write("### Growth Strategist VC (Scaling & GTM)")
                st.write(growth_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Enter your startup details and API key, then click 'Get VC Feedback' to receive insights.")

import streamlit as st
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

# Load API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Define Backend Agent
backend_agent = Agent(
    name="Backend Agent",
    role="Generate professional backend code.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Decide the best backend language/framework based on requirements.",
        "Generate professional-level code in Node.js, Django, Flask, FastAPI, Spring Boot, Laravel, CodeIgniter, Ruby on Rails, ASP.NET Core, Go, Rust, or Kotlin.",
        "Ensure scalability, security, and clean architecture.",
    ],
    markdown=True,
)

# Define Backend Docker Agent
backend_docker_agent = Agent(
    name="Backend Docker Agent",
    role="Generate Dockerfile for the backend.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Generate an optimized Dockerfile for the backend.",
        "Ensure best practices like small image size and environment variable security.",
    ],
    markdown=True,
)

# Define Frontend Agent
frontend_agent = Agent(
    name="Frontend Agent",
    role="Generate professional frontend code.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Decide the best frontend language/framework based on requirements.",
        "Generate professional-level code in HTML, CSS, JavaScript, TypeScript, React, Vue, Angular, or Svelte.",
        "Ensure clean, maintainable, and well-documented code.",
    ],
    markdown=True,
)

# Define Frontend Docker Agent
frontend_docker_agent = Agent(
    name="Frontend Docker Agent",
    role="Generate Dockerfile for the frontend.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Generate an optimized Dockerfile for the frontend.",
        "Ensure best practices like multi-stage builds if necessary.",
    ],
    markdown=True,
)

# Streamlit UI
st.title("Multi-Agent AI Code Generator 🚀")
st.subheader("Generate Full-Stack Code and Dockerfiles Using AI Agents")

project_description = st.text_area("Describe your project requirements:", "")

if st.button("Generate Code"):
    if project_description:
        with st.spinner("Generating Frontend Code..."):
            frontend_code = frontend_agent.run(project_description).content
        
        with st.spinner("Generating Backend Code..."):
            backend_code = backend_agent.run(project_description).content

        with st.spinner("Generating Frontend Dockerfile..."):
            frontend_dockerfile = frontend_docker_agent.run(frontend_code).content

        with st.spinner("Generating Backend Dockerfile..."):
            backend_dockerfile = backend_docker_agent.run(backend_code).content

        st.success("Code Generation Complete!")
        
        st.subheader("Frontend Code:")
        st.code(frontend_code, language="javascript")

        st.subheader("Backend Code:")
        st.code(backend_code, language="python")

        st.subheader("Frontend Dockerfile:")
        st.code(frontend_dockerfile, language="docker")

        st.subheader("Backend Dockerfile:")
        st.code(backend_dockerfile, language="docker")
    
    else:
        st.warning("Please enter a project description.")

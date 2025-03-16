# AI-Agents-Chatbot-Langchain
# LangGraph Agent UI

A modular web application that provides a professional interface to interact with AI chatbot agents. This project integrates a customizable AI agent with support for multiple models (Groq and OpenAI) and optional web search capabilities.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

---

## Overview

LangGraph Agent UI offers users a streamlined interface to communicate with AI agents. With a sleek frontend built on Streamlit and a robust backend using FastAPI, the system enables real-time chat interactions, dynamic model selection, and optional web search integration to enrich responses.

---

## Features

- **Multiple Model Support:** Choose between Groq and OpenAI models.
- **Customizable Prompts:** Define system prompts to steer agent behavior.
- **Web Search Integration:** Enable web search tools for enhanced responses.
- **Professional UI:** Modern and intuitive user interface with images and organized layouts.
- **API-Driven:** FastAPI backend for efficient communication and error handling.
- **Dynamic Agent Interaction:** Real-time processing and robust error handling for API calls.

---

## Technologies

- **Frontend:** Python, Streamlit, Requests
- **Backend:** FastAPI, Pydantic, Uvicorn
- **AI Integration:** LangChain, LangGraph, and community search tools
- **Other:** dotenv for environment configuration

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### Setup Steps

1. **Clone the repository:**

   ```bash
      git clone https://github.com/mayurdalvi5/AI-Agents-Chatbot-Langchain/.git
      cd AI-Agents-Chatbot-Langchain
A modular web application that provides a professional interface to interact with AI chatbot agents. This project integrates a customizable AI agent with support for multiple models (Groq and OpenAI) and optional web search capabilities.

2. **Create and activate a virtual environment:**
    ```bash
       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   ```bash
      pip install -r requirements.txt

4. **Set up environment variables:**
    Create a `.env` file in the project root and add any necessary variables (e.g., API keys).

---

## Usage

### Running the Backend

  - Start the FastAPI server by running
  ```bash
     python backend.py
  ```
  - This will run the server on http://127.0.0.1:9999.

### Running the Frontend

  - In a new terminal, launch the Streamlit application:
  ```bash
     streamlit run frontend.py
  ```
  - Open your browser and navigate to the provided URL (usually http://localhost:8501) to interact with the UI.

---

## Project Structure
   ```bash
      langgraph-agent-ui/
        ├── ai_agent.py         # AI agent logic and integration with LangChain tools
        ├── backend.py          # FastAPI backend for handling chat requests and API endpoints
        ├── frontend.py         # Streamlit frontend for user interaction and UI rendering
        ├── requirements.txt    # List of project dependencies
        ├── README.md           # Project documentation and usage instructions
        └── .env                # Environment variables configuration file (not tracked by version control)
  ```





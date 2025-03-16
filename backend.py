# backend.py
# =============================================================================
# Import required libraries and modules
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException
import uvicorn  # For running the server
from ai_agent import get_response_from_ai_agent  # Import AI response function

# -----------------------------------------------------------------------------
# Define request schema using Pydantic for data validation
class RequestState(BaseModel):
    model_name: str         # Name of the AI model
    model_provider: str     # Provider type ("Groq" or "OpenAI")
    system_prompt: str      # Prompt that defines the agent behavior
    messages: List[str]     # List of messages (queries) from the user
    allow_search: bool      # Flag to allow web search functionality

# -----------------------------------------------------------------------------
# List of allowed model names for validation
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192", 
    "mixtral-8x7b-32768", 
    "llama-3.3-70b-versatile", 
    "gpt-4o-mini"
]

# -----------------------------------------------------------------------------
# Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent")

# -----------------------------------------------------------------------------
# Define the API endpoint to handle chat requests
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It validates the request and dynamically selects the model specified.
    """
    # Validate model name
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(status_code=400, detail="Invalid model name. Kindly select a valid AI model")
    
    # Extract request data
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Attempt to get a response from the AI agent
    try:
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    except Exception as e:
        # Return error details if the agent invocation fails
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")

    # Return the AI agent's response as JSON
    return {"response": response}

# -----------------------------------------------------------------------------
# Run the FastAPI app with Uvicorn when this script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)

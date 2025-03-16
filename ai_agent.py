# ai_agent.py
# =============================================================================
# Import required modules and load environment variables
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Load environment variables from .env file
load_dotenv()

# -----------------------------------------------------------------------------
# Pre-initialize LLMs for potential reuse (optional caching)
openai_llm = ChatOpenAI(model='gpt-40-min')
groq_llm = ChatGroq(model='llama-3.3-70b-versatile')

# -----------------------------------------------------------------------------
def get_response_from_ai_agent(llm_id: str, query: list, allow_search: bool, system_prompt: str, provider: str) -> str:
    """
    Create an AI agent with the provided parameters and return the agent's response.
    
    Parameters:
        llm_id (str): Identifier of the selected model.
        query (list): List of user messages.
        allow_search (bool): Flag to include web search capabilities.
        system_prompt (str): Instructional prompt for the AI agent.
        provider (str): Model provider ("Groq" or "OpenAI").
        
    Returns:
        str: The final response from the AI agent.
    """
    # Select the appropriate LLM based on the provider
    if provider == 'Groq':
        llm = ChatGroq(model=llm_id)
    elif provider == 'OpenAI':
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Unsupported provider specified.")

    # Setup tools list if web search is allowed
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create the AI agent using the selected LLM and tools
    agent = create_react_agent(
        model=llm,              # Use the dynamically chosen LLM (bug fix: using llm instead of a static groq_llm)
        tools=tools,            # Attach search tools if enabled
        state_modifier=system_prompt  # Apply the system prompt to modify agent behavior
    )

    # Define the initial state with the user messages
    state = {'messages': query}

    # Invoke the agent and obtain a response
    response = agent.invoke(state)

    # Extract AI messages from the response (assuming response contains a "messages" list)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    # Return the last AI message as the final response
    if ai_messages:
        return ai_messages[-1]
    else:
        raise ValueError("No AI response was generated.")

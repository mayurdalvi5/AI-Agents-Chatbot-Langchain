# frontend.py
# =============================================================================
# Import required libraries
import streamlit as st
import requests  # For API calls

# -----------------------------------------------------------------------------
# Configure the Streamlit page settings for a professional look
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# -----------------------------------------------------------------------------
# Sidebar for additional options (optional enhancement)
st.sidebar.header("Agent Configuration")
system_prompt = st.sidebar.text_area(
    "Define your AI Agent:",
    height=70,
    placeholder="Type your system prompt here..."
)  # System prompt to guide AI behavior

# -----------------------------------------------------------------------------
# Define available models for each provider
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# -----------------------------------------------------------------------------
# Provider selection using radio buttons
provider = st.sidebar.radio("Select Provider:", ("Groq", "OpenAI"))

# Conditional model selection based on provider
if provider == "Groq":
    selected_model = st.sidebar.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
else:  # provider == "OpenAI"
    selected_model = st.sidebar.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

# -----------------------------------------------------------------------------
# Option to allow web search functionality
allow_web_search = st.sidebar.checkbox("Allow Web Search")

# -----------------------------------------------------------------------------
# Main text area for user query input
user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask Anything!"
)

# -----------------------------------------------------------------------------
# Define API endpoint URL
API_URL = "http://127.0.0.1:9999/chat"

# -----------------------------------------------------------------------------
# Button to trigger the agent request; wrapped in a spinner for better UX
if st.button("Ask Agent!"):
    if user_query.strip():
        # Display a loading spinner while processing the request
        with st.spinner("Waiting for the agent's response..."):
            # Prepare the JSON payload for the backend API
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }
            try:
                # Post the request to the backend
                response = requests.post(API_URL, json=payload, timeout=10)
                response.raise_for_status()  # Raise exception for HTTP errors

                # Parse the JSON response
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent Response")
                    # Display final response with proper formatting
                    st.markdown(f"**Final Response:** {response_data}")
            except requests.RequestException as e:
                # Handle network errors gracefully
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before submitting.")

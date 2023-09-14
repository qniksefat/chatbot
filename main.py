import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv, find_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Define the language model
language_model = "gpt-3.5-turbo-0301"

# Load environment variables
load_dotenv(find_dotenv())

# Set up OpenAI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Configure Streamlit page
st.set_page_config(page_title="ChatBot", page_icon="🤖")

if __name__ == "__main__":
    
    # Initialize the chat model
    chat_model = ChatOpenAI(temperature=0, model=language_model)

    # Initialize message history if not present in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    st.header("ChatBot")

    # User input in the main section
    user_input = st.text_input("Your message: ", key="user_input")

    # Handle user input
    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Thinking..."):
            response = chat_model(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        
    # Display message history
    messages = st.session_state.get('messages', [])
    
    for msg in messages[1:][1::2]:
        message(msg.content)

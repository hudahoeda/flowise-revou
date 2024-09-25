import os
import streamlit as st
from Home import login,load_flowise_chat_screen, generate_custom_api_response
import uuid

# Main content
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    login()
else:
    # Using your custom API URL and Authorization header
    API_URL = os.environ.get('FLOWISE_ENDPOINT')
    headers = {"Authorization": os.environ.get('FLOWISE_KEY')}  # Use your actual key here
    assistant_message = "TL Assistant is here to help you with your queries. Please type your query below."
    assistant_title = "TL Assistant"
    
    # Use the modified Flowise chat screen loader
    load_flowise_chat_screen(API_URL, headers, assistant_title, assistant_message)
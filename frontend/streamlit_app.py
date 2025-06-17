import streamlit as st
import requests
import os

st.title("Participant Advisor Bot")

user_id = st.text_input("Enter User ID")
query = st.text_area("Ask a question")

if st.button("Send") and user_id and query:
    headers = {"Authorization": f"Bearer {os.getenv('SECRET_KEY', 'your-secret-key-here')}"}
    payload = {"user_id": user_id, "query": query}
    response = requests.post("http://backend:8000/advisor/query", json=payload, headers=headers)
    st.write(response.json())
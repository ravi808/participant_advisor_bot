import streamlit as st
import requests

st.title("Participant Advisor Bot")

user_id = st.text_input("Enter User ID")
query = st.text_area("Ask a question")

if st.button("Send") and user_id and query:
    headers = {"Authorization": "Bearer your-secret-key-here"}
    payload = {"user_id": user_id, "query": query}
    response = requests.post("http://localhost:8000/advisor/query", json=payload, headers=headers)
    st.write(response.json())
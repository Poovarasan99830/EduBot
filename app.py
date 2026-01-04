import streamlit as st
from chatbot.bot_core import create_edubot

st.title("🎓 EduBot — AI Teaching Assistant")

chat = create_edubot()

user_input = st.text_input("Ask EduBot anything about Python, AI, or programming:")

if user_input:
    response = chat(user_input)
    st.markdown(f"**EduBot:** {response}")



# streamlit run app.py

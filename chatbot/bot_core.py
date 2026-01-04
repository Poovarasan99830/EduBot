
# chatbot/bot_core.py (sketch)
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_KEY:
    raise RuntimeError("GROQ_API_KEY missing. Set it in .env or your environment variables.")

def create_edubot(model="llama-3.1-8b-instant", temperature=0.7):

    llm = ChatGroq(
                   model=model, 
                   api_key=GROQ_KEY, 
                   temperature=temperature
                   )


    history = ChatMessageHistory()

    def chat(message):
        history.add_user_message(message)
        messages = [
            AIMessage("You are EduBot, a friendly AI teaching assistant. Keep answers clear and short.")
        ] + history.messages + [HumanMessage(content=message)]
        try:
            response = llm.invoke(messages)
            history.add_ai_message(response.content)
            return response.content
        except Exception as e:
            # Log e (to file/console) and return a friendly fallback
            print("LLM error:", e)
            return "Sorry — the model is currently unavailable. Try again later."

    return chat

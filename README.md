

# 🚀 EduBot – AI Teaching Chatbot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![LLM](https://img.shields.io/badge/LLM-LLaMA3.1-green)
![API](https://img.shields.io/badge/API-Groq-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

**EduBot** is an AI-powered teaching chatbot that helps students learn concepts interactively.

It can:

*  Answer questions
*  Explain concepts
*  Help with coding
*  Maintain conversation context

---

##  Features

✅ AI-powered responses using LLM
✅ Fast replies using Groq API ⚡
✅ Chat memory (context-aware answers)
✅ Simple UI using Streamlit
✅ Secure API key handling (`.env`)
✅ Scalable for RAG & advanced AI features

---

##  Architecture

```
User → Streamlit UI → Backend (LangChain) → Groq API → LLM → Response → UI
```

---

##  Tech Stack

| Layer     | Technology |
| --------- | ---------- |
| UI        | Streamlit  |
| Backend   | Python     |
| LLM       | LLaMA 3.1  |
| Framework | LangChain  |
| API       | Groq       |

---

## Project Structure

```
EduBot/
│
├── app.py                 # Streamlit UI
├── chatbot/
│   └── bot_core.py       # LLM logic
├── .env                  # API keys (hidden)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/edubot.git
cd edubot
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## How It Works

1. User enters a question
2. Streamlit sends input to backend
3. LangChain processes the prompt
4. Request sent to Groq API
5. LLaMA model generates response
6. Answer displayed to user

---

## Key Concepts Used

### 🔹 LLM (Large Language Model)

* Generates human-like responses
* Example: LLaMA 3.1

### 🔹 Tokens

* Small units of text
* Affect cost & performance

### 🔹 Context Window

* Memory size of the model

### 🔹 Temperature

* Controls creativity of output

### 🔹 Prompt Engineering

* Writing better inputs → better outputs

### 🔹 API Key Security

* Stored in `.env`
* Prevents exposure



##  Advanced Concepts (Future Scope)

* PDF Chatbot (RAG)
* Embeddings & Vector DB
* Voice-based chatbot
* Multi-language support

---

## Limitations

* May give incorrect answers
* Depends on prompt quality
* Limited memory (context window)

---

## Interview Points

* Difference between API & Model
* Role of LangChain
* What is RAG
* Tokens & Context Window
* Temperature tuning
* Ollama vs Groq

---

## Conclusion

EduBot demonstrates:

✅ LLM integration
✅ API-based architecture
✅ Chatbot with memory
✅ Real-world AI application


## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Improve & contribute



## Author

Poovarasan                                                                        
Manikandan                                                                     
Vainavin

🚀 Python Full Stack Developer
🤖 AI-Integrated Application Developer





Further reference use below link:

https://chatgpt.com/s/t_69cbfaced56481918fddd343c192537b 
https://chatgpt.com/s/t_69cbfaee2fb48191991aaca1e7a665b4


https://chatgpt.com/share/69d32d61-03bc-83e8-87a6-72995234acbf




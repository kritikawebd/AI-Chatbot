import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot (TinyLlama + Ollama)")
st.markdown("Chat privately and locally using your own machine!")

# Chat history storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for modes (if needed later)
# st.sidebar.title("Settings")

# User input
prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    try:
        # Send prompt to local Ollama instance
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "tinyllama", "messages": st.session_state.messages}
        )

        reply = response.json()["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"❌ Failed to connect to Ollama. Make sure it is running locally.\n\nError: {e}")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

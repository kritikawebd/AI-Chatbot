import streamlit as st
from ollama import Client
import random

# Page setup (keep your beautiful UI)
st.set_page_config(page_title="Kritika Kasera Chatbot 💡", layout="wide")

# Stylish Header (preserved exactly)
st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(to right, #fce4ec, #f8bbd0); border-radius: 16px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);'>
        <h1 style='color: #880e4f;'>💬 Kritika Kasera Chatbot</h1>
        <p style='font-size: 18px; color: #4a148c;'>An AI-powered assistant for learning, chatting & emotional support.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar (unchanged)
with st.sidebar:
    st.title("⚙️ Mode Selector")
    chat_mode = st.radio("Choose Chat Mode:", ["🧠 Free Chat", "🎓 Guided Learning"])
    st.markdown("---")
    st.markdown("Built with ❤️ by **Kritika Kasera**")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Modified AI response generator
def get_ai_response(messages, model="tinyllama"):
    try:
        client = Client(host='http://localhost:11434')
        response = client.chat(
            model=model,
            messages=messages,
            stream=True
        )
        for chunk in response:
            if chunk.get("message") and "content" in chunk["message"]:
                yield chunk["message"]["content"]
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        fallbacks = [
            "🌸 Please run locally with Ollama for full features!",
            "💡 Install Ollama and run: ollama pull tinyllama",
            "📚 Guided mode works best with local AI setup",
            "🔌 Demo mode active - connect Ollama locally"
        ]
        yield random.choice(fallbacks)

# Chat input handling
if prompt := st.chat_input(f"Ask something in {chat_mode.split()[1]} mode..."):
    # User message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Add guided learning prompt if needed
        if "Guided" in chat_mode:
            st.session_state.messages[-1]["content"] = (
                "You are a helpful tutor. Please guide step-by-step:\n\n" +
                st.session_state.messages[-1]["content"]
            )

        # Stream response
        for chunk in get_ai_response(st.session_state.messages):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
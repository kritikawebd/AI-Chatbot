import streamlit as st
import random

# ======================
# 🌸 Beautiful UI Setup
# ======================
st.set_page_config(
    page_title="Kritika Kasera Chatbot 💡", 
    layout="wide",
    menu_items={
        'About': "Built with ❤️ by Kritika Kasera"
    }
)

# Gradient header with your exact styling
st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(to right, #fce4ec, #f8bbd0); border-radius: 16px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);'>
        <h1 style='color: #880e4f;'>💬 Kritika Kasera Chatbot</h1>
        <p style='font-size: 18px; color: #4a148c;'>An AI-powered assistant for learning, chatting & emotional support.</p>
    </div>
""", unsafe_allow_html=True)

# ======================
# ⚙️ Sidebar Controls
# ======================
with st.sidebar:
    st.title("⚙️ Mode Selector")
    chat_mode = st.radio(
        "Choose Chat Mode:", 
        ["🧠 Free Chat", "🎓 Guided Learning"],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    **Local Setup Guide:**  
    1. Install [Ollama](https://ollama.ai)  
    2. Run: `ollama pull tinyllama`  
    """)

# ======================
# 🧠 AI Core Function
# ======================
def get_ai_response(messages):
    """Universal function that works everywhere"""
    try:
        from ollama import Client
        client = Client(host='http://localhost:11434', timeout=10)
        response = client.chat(
            model="tinyllama",
            messages=messages,
            stream=True
        )
        for chunk in response:
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content
    except:
        yield random.choice([
            "🌸 For full features, please run locally with Ollama!",
            "💡 Tip: Install Ollama and run `ollama pull tinyllama`",
            "🔌 (Psst! I'm in demo mode - connect local Ollama for full power)"
        ])

# ======================
# 💬 Chat Interface
# ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your AI assistant. Ready to chat?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new input
if prompt := st.chat_input(f"Message in {chat_mode.split()[1]} mode..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Prepare prompt for guided mode
    if "Guided" in chat_mode:
        prompt = "You are a helpful tutor. Guide step-by-step:\n\n" + prompt
    
    # Get and display AI response
    with st.chat_message("assistant"):
        response = st.write_stream(
            get_ai_response(st.session_state.messages)
        )
    
    # Save to history
    st.session_state.messages.append({"role": "assistant", "content": response})
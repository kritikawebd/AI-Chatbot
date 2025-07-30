import streamlit as st
from ollama import Client

# Page setup
st.set_page_config(page_title="Kritika Kasera Chatbot 💡", layout="wide")

# Stylish Header
st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(to right, #fce4ec, #f8bbd0); border-radius: 16px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);'>
        <h1 style='color: #880e4f;'>💬 Kritika Kasera Chatbot</h1>
        <p style='font-size: 18px; color: #4a148c;'>An AI-powered assistant for learning, chatting & emotional support.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar for selecting chat mode
with st.sidebar:
    st.title("⚙️ Mode Selector")
    chat_mode = st.radio("Choose Chat Mode:", ["🧠 Free Chat", "🎓 Guided Learning"])
    st.markdown("---")
    st.markdown("Built with ❤️ by **Kritika Kasera**")

# Initialize Ollama client (make sure Ollama and `tinyllama` are pulled)
client = Client(host='http://localhost:11434')

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from user
prompt = st.chat_input(f"Ask something in {chat_mode.split()[1]} mode...")

if prompt:
    # Display user input
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # Assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Use lighter model to prevent memory issues
        model_name = "tinyllama"

        # Modify prompt for Guided Learning
        if "Guided" in chat_mode:
            guided_intro = "You are a helpful tutor. Please guide the user step-by-step:\n\n"
            st.session_state.messages[-1]["content"] = guided_intro + prompt

        # Stream response
        try:
            response = client.chat(
                model=model_name,
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in response:
                if "message" in chunk and "content" in chunk["message"]:
                    full_response += chunk["message"]["content"]
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
        except Exception as e:
            message_placeholder.error(f"⚠️ Error: {e}")
            st.stop()

    # Save response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
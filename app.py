import streamlit as st
from ollama import Client
import time
import subprocess

# 💻 Attempt to start Ollama server
try:
    subprocess.Popen(["ollama", "serve"])
except Exception as e:
    st.error(f"⚠️ Could not start Ollama server: {e}")

# 🧠 Page settings
st.set_page_config(page_title="Kritika's AI Assistant", page_icon="🤖", layout="centered")

# 🌈 Header Design
st.markdown(
    """
    <h1 style='text-align: center; color: #6C63FF;'>🤖 Kritika's Local AI Chatbot</h1>
    <p style='text-align: center; color: #888;'>⚡ 100% Offline – Powered by Ollama + TinyLlama</p>
    <hr style="border:1px solid #ddd;">
    """,
    unsafe_allow_html=True,
)

# 🎯 Connect to Ollama server
client = Client(host='http://127.0.0.1:11434')

# 💬 Chat functionality
prompt = st.chat_input("💬 Type your question here...")

if prompt:
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    with st.chat_message("assistant"):
        try:
            # Verify connection
            client.list()

            full_response = ""
            output_area = st.empty()

            thinking_animation = st.markdown("🤔 Thinking...")
            time.sleep(0.5)

            for chunk in client.chat(
                model="tinyllama",
                messages=[{"role": "user", "content": prompt}],
                stream=True
            ):
                full_response += chunk.get("message", {}).get("content", "")
                output_area.markdown(f"**AI:** {full_response}▌")
                time.sleep(0.01)

            thinking_animation.empty()
            output_area.markdown(f"**AI:** {full_response}")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# 🎨 Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: grey; font-size: small;'>Made with 💜 by Kritika Kasera</p>
    """,
    unsafe_allow_html=True,
)

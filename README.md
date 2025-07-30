# 🧠 Kritika's Local AI Chatbot

A simple offline chatbot powered by [Ollama](https://ollama.com) and Streamlit.  
No internet needed after setup. Your data stays 100% private.

---

## ✅ Features

- Fully offline after setup
- Uses `tinyllama` (or any Ollama model)
- Clean interface with Streamlit
- Real-time response streaming
- Works on CPU or GPU

---

## 🛠️ Setup Instructions

1. Install Ollama from: https://ollama.com/download  
2. Pull a model (e.g., tinyllama):
   ```bash
   ollama pull tinyllama
   ```
3. Install Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

---

## 📦 Requirements

- Python 3.8+
- Ollama installed
- Model pulled via Ollama (e.g., `tinyllama`)

---

💡 Works offline once the model is downloaded. Ideal for privacy-focused use.

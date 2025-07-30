# 🔹 Kritika's AI Chatbot  
**By Kritika Kasera**  

🌸 *Local-first chatbot with graceful cloud fallbacks*  

---

## ✨ Features  

### Local Mode (Full Power)  
- 🗣️ **Free Chat** with TinyLlama (1.1B) via Ollama  
- 🎓 **Guided Learning** with step-by-step tutoring  
- 🔒 **100% Private** - No data leaves your device  

### Cloud Mode (Demo)  
- 🌐 **Friendly Placeholders** when Ollama isn't available  
- 💡 **Setup Instructions** embedded in responses  

---

## 🛠️ Tech Stack  

| Component        | Local Mode         | Cloud Mode         |  
|------------------|--------------------|--------------------|  
| AI Engine        | Ollama + TinyLlama | Streamlit Fallbacks|  
| Inference        | On your device     | Demo messages      |  
| Requirements     | Python 3.8+, Ollama| Python 3.8+        |  

---

## 🚀 Installation  

### 1. For Full Experience (Local)  
```bash
# Install Ollama  
curl -fsSL https://ollama.ai/install.sh | sh  # Linux/macOS  
winget install ollama                         # Windows  

# Get model  
ollama pull tinyllama  

# Run chatbot  
streamlit run app.py  
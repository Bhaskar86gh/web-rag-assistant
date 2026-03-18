# 🔥 Web RAG AI Assistant

An intelligent AI-powered system that allows users to **extract, understand, and query website content** using Retrieval-Augmented Generation (RAG).

---

## 🌐 What This Project Does

This system enables you to:

- 🔗 Ingest any website URL
- 🧠 Convert website content into embeddings
- 🔍 Perform semantic search
- 🤖 Ask natural language questions
- ✅ Get accurate, context-based answers (NO hallucination)

---

## ⚡ Key Features

- 🌍 Website content ingestion (BeautifulSoup)
- 🧩 Smart text chunking
- 🧠 Semantic embeddings (Sentence Transformers)
- 🔎 FAISS vector search
- 🎯 Relevance filtering (reduces noise)
- 🤖 LLM-based answer generation (Ollama)
- ⚡ FastAPI backend with Swagger UI

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|-----------|
| Backend | FastAPI |
| Vector DB | FAISS |
| Embeddings | Sentence Transformers |
| LLM | Ollama (LLaMA3) |
| Scraping | BeautifulSoup |
| Language | Python |

---

## 📂 Project Structure
# 🔥 Web RAG AI Assistant

An intelligent AI-powered system that allows users to **extract, understand, and query website content** using Retrieval-Augmented Generation (RAG).

---

## 🌐 What This Project Does

This system enables you to:

- 🔗 Ingest any website URL
- 🧠 Convert website content into embeddings
- 🔍 Perform semantic search
- 🤖 Ask natural language questions
- ✅ Get accurate, context-based answers (NO hallucination)

---

## ⚡ Key Features

- 🌍 Website content ingestion (BeautifulSoup)
- 🧩 Smart text chunking
- 🧠 Semantic embeddings (Sentence Transformers)
- 🔎 FAISS vector search
- 🎯 Relevance filtering (reduces noise)
- 🤖 LLM-based answer generation (Ollama)
- ⚡ FastAPI backend with Swagger UI

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|-----------|
| Backend | FastAPI |
| Vector DB | FAISS |
| Embeddings | Sentence Transformers |
| LLM | Ollama (LLaMA3) |
| Scraping | BeautifulSoup |
| Language | Python |

---

## 📂 Project Structure
web-rag/
│
├── api/
│ └── routes.py
├── automation/
│ └── scraper.py
├── llm/
│ └── ollama_client.py
├── rag/
│ ├── chunker.py
│ ├── embeddings.py
│ ├── pdf_loader.py
│ ├── vector_store.py
│
├── main.py
├── requirements.txt
├── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/web-rag-assistant.git
cd web-rag-assistant
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Ollama (LLM)
ollama run llama3
5️⃣ Start the Server
uvicorn main:app --reload
📡 API Usage

Open Swagger UI:

http://127.0.0.1:8000/docs
🔗 1. Ingest Website

Endpoint: /ingest_website

Example:

https://example.com
❓ 2. Ask Questions

Endpoint: /ask

Example Questions:

What is this website about?

What services does this website provide?

Summarize the main purpose of this website

What topics are covered here?

📊 3. Check Status

Endpoint: /status

🧠 How It Works

Website is scraped → meaningful text extracted

Text is split into chunks

Each chunk → converted into embeddings

Stored in FAISS vector database

User query → converted into embedding

Top relevant chunks retrieved

LLM generates context-aware answer

🚨 Limitations

❌ Dynamic websites (YouTube, Instagram) may not work well

❌ No JavaScript rendering (static scraping only)

❌ Depends on quality of website content

🔥 Future Improvements

✅ YouTube transcript support

✅ Multi-URL ingestion

✅ Hybrid search (keyword + semantic)

✅ Chat UI (frontend)

✅ Persistent vector database

👨‍💻 Author

Bhaskar

⭐ If You Like This Project

Give it a ⭐ on GitHub and share it!

## 📸 Demo Screenshots

![Screenshot 1](screenshots/weblink.png)
![Screenshot 2](screenshots/answer.png)

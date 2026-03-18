from fastapi import FastAPI, UploadFile, File
from typing import List
from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import embed_documents, embed_query
from rag.vector_store import create_index, search
from llm.ollama_client import generate
from automation.scraper import scrape_website

app = FastAPI()

# GLOBAL STORAGE
documents = []
index = None


# ---------------- PDF UPLOAD ----------------
@app.post("/upload_pdf")
async def upload_pdf(files: List[UploadFile] = File(...)):
    global documents, index

    all_chunks = []
    filenames = []

    for file in files:
        content = await file.read()

        text = load_pdf(content)
        chunks = chunk_text(text)

        all_chunks.extend(chunks)
        filenames.append(file.filename)

    if not all_chunks:
        return {"error": "No text extracted from PDFs"}

    embeddings = embed_documents(all_chunks)
    index = create_index(embeddings)

    documents = all_chunks

    return {
        "message": "PDFs processed successfully",
        "files": filenames,
        "total_chunks": len(all_chunks)
    }


# ---------------- WEBSITE INGEST ----------------
@app.post("/ingest_website")
def ingest_website(url: str):
    global documents, index

    text = scrape_website(url)

    if not text or "Error" in text:
        return {"error": text}

    chunks = chunk_text(text)

    if not chunks:
        return {"error": "No content extracted from website"}

    embeddings = embed_documents(chunks)
    index = create_index(embeddings)

    documents = chunks

    return {
        "message": "Website ingested successfully",
        "url": url,
        "total_chunks": len(chunks)
    }


# ---------------- ASK ----------------
@app.get("/ask")
def ask(q: str):
    global documents, index

    if index is None or not documents:
        return {"error": "No data loaded yet"}

    # 🔹 Embed query
    query_embedding = embed_query(q)

    # 🔹 Search (now returns scores)
    results = search(index, query_embedding, k=10)

    # 🔹 Filter relevant chunks
    filtered = [r for r in results if r["score"] > 0.3]

    # fallback if nothing passes filter
    if not filtered:
        filtered = results[:3]

    # 🔹 Pick top chunks
    top_chunks = filtered[:5]

    # 🔹 Build context
    context_chunks = [
        documents[r["index"]]
        for r in top_chunks
        if r["index"] < len(documents)
    ]

    context = "\n\n".join(context_chunks)

    # 🔥 STRONG PROMPT (KEY FIX)
    prompt = f"""
You are an intelligent AI assistant.

Rules:
- Answer ONLY from the given context
- Be SPECIFIC and FACTUAL
- Do NOT give generic answers
- If answer is unclear, say: "Not enough information available"

Context:
{context}

Question:
{q}

Answer (clear and precise):
"""

    # 🔹 Generate answer (low temperature recommended)
    answer = generate(prompt)

    return {"answer": answer}


# ---------------- STATUS ----------------
@app.get("/status")
def status():
    return {
        "documents_loaded": len(documents),
        "index_ready": index is not None
    }
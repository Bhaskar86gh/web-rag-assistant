from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


# 🔹 Embed multiple documents
def embed_documents(texts):
    return model.encode(texts)


# 🔹 Embed single query
def embed_query(text):
    return model.encode([text])[0]
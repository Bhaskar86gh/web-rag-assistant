import faiss
import numpy as np

# Global index + store embeddings
index = None
stored_embeddings = None


# 🔹 Create FAISS index
def create_index(embeddings):
    global index, stored_embeddings

    embeddings = np.array(embeddings).astype("float32")
    stored_embeddings = embeddings

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index


# 🔹 Search similar chunks WITH SCORES
def search(index, query_embedding, k=10):
    global stored_embeddings

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for i, idx in enumerate(indices[0]):
        if idx == -1:
            continue

        score = float(distances[0][i])

        # Convert L2 distance → similarity (lower = better)
        similarity = 1 / (1 + score)

        results.append({
            "index": int(idx),
            "score": similarity
        })

    # Sort by best similarity
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results
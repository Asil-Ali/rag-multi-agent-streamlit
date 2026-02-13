from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
documents = []

def load_documents(files):
    global documents
    for file in files:
        text = file.read().decode("utf-8", errors="ignore")
        documents.append(text)
        emb = model.encode([text])
        index.add(emb)

def retrieve(query):
    emb = model.encode([query])
    _, ids = index.search(emb, 2)
    return "\n".join([documents[i] for i in ids[0] if i < len(documents)])

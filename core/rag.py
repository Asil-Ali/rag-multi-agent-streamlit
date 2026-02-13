import os
import faiss
from sentence_transformers import SentenceTransformer
import pypdf
import streamlit as st

# إعداد نموذج التحويل embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)  # الأبعاد تعتمد على النموذج
documents = []

def load_documents(user_files=[]):
    """
    قراءة ملفات PDF الجاهزة + ملفات المستخدم
    """
    global documents

    # 1️⃣ قراءة كل PDF في مجلد data/uploads
    preloaded_path = "data/uploads"
    for filename in os.listdir(preloaded_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(preloaded_path, filename)
            try:
                with open(file_path, "rb") as f:
                    reader = pypdf.PdfReader(f)
                    text = ""
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text
                    if text:
                        documents.append(text)
                        emb = model.encode([text])
                        index.add(emb)
                    else:
                        print(f"Warning: {filename} لا يحتوي على نص يمكن قراءته.")
            except Exception as e:
                print(f"Failed to read {filename}: {e}")

    # 2️⃣ قراءة ملفات يرفعها المستخدم عبر Streamlit
    for file in user_files:
        try:
            # قراءة الملف كـ PDF (يمكن تعديل لو عندك ملفات نصية)
            reader = pypdf.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            if text:
                documents.append(text)
                emb = model.encode([text])
                index.add(emb)
        except Exception as e:
            print(f"Failed to read uploaded file {file.name}: {e}")

def search(query, top_k=3):
    """
    البحث في الـ RAG index
    """
    if not documents:
        return []

    query_emb = model.encode([query])
    D, I = index.search(query_emb, top_k)
    results = [documents[i] for i in I[0] if i < len(documents)]
    return results

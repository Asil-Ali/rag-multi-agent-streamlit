import os
import streamlit as st
from core.rag import load_documents, search

st.set_page_config(page_title="RAG Multi-Agent Demo", layout="wide")
st.title("RAG Multi-Agent Streamlit")

# التحقق من وجود ملفات PDF جاهزة
uploads_path = "data/uploads"
if not os.path.exists(uploads_path):
    st.error(f"Error: المجلد {uploads_path} غير موجود!")
elif not any(f.lower().endswith(".pdf") for f in os.listdir(uploads_path)):
    st.warning("لا توجد ملفات PDF جاهزة في uploads/ للتحميل.")

# رفع ملفات PDF جديدة من المستخدم
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

# تحميل الملفات الجاهزة + الملفات المرفوعة
load_documents(user_files=uploaded_files)

# مربع بحث
query = st.text_input("Ask something about the documents:")

if query:
    results = search(query, top_k=3)
    if results:
        for i, res in enumerate(results, start=1):
            st.markdown(f"### Result {i}")
            st.write(res[:1000] + "...")  # عرض أول 1000 حرف فقط
    else:
        st.write("No results found.")

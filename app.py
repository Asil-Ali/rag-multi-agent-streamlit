import os
import streamlit as st
from core.rag import load_documents

st.set_page_config(page_title="RAG Multi-Agent Demo", layout="wide")
st.title("RAG Multi-Agent Streamlit")

# التحقق من وجود ملفات PDF أو TXT جاهزة
uploads_path = "data/uploads"
if not os.path.exists(uploads_path):
    st.error(f"Error: المجلد {uploads_path} غير موجود!")
elif not any(f.lower().endswith(".pdf") or f.lower().endswith(".txt") for f in os.listdir(uploads_path)):
    st.warning("لا توجد ملفات جاهزة في uploads/ للتحميل.")

# رفع ملفات PDF أو TXT جديدة من المستخدم
uploaded_files = st.file_uploader(
    "Upload PDF/TXT files",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

# تحميل الملفات الجاهزة + الملفات المرفوعة
load_documents(user_files=uploaded_files)

# مربع البحث
query = st.text_input("Ask something about the documents:")

# اختيار الـ Agent
agent_choice = st.selectbox("Choose Agent", ["Summarizer", "FAQ", "Marketing"])

if query:
    if agent_choice == "Summarizer":
        from agents.summarizer_agent import summarize_document
        st.write(summarize_document(query))
    elif agent_choice == "FAQ":
        from agents.faq_agent import answer_question
        st.write(answer_question(query))
    elif agent_choice == "Marketing":
        from agents.marketing_agent import marketing_insights
        st.write(marketing_insights(query))

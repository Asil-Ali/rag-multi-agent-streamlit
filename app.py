import streamlit as st
from core.orchestrator import run_app
from core.rag import load_documents

st.set_page_config(page_title="RAG Multi-Agent AI")

st.title("RAG Multi-Agent AI System")

uploaded_files = st.file_uploader(
    "Upload your knowledge files",
    type=["pdf", "txt", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    load_documents(uploaded_files)
    st.success("Files processed successfully")

query = st.text_area("Ask your question")

if st.button("Run"):
    if query:
        with st.spinner("Thinking..."):
            answer = run_app(query)
            st.write(answer)

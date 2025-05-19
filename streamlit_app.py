import streamlit as st
import tempfile
import os
import shutil
from pathlib import Path
from backend import load_and_process_pdfs, initialize_vectorstore, get_chunks_and_answer



st.set_page_config(page_title="Document RAG Chatbot", layout="wide")
st.title("📄 Document RAG Chatbot")

# Sidebar - Upload multiple files
st.sidebar.header("📤 Upload Documents")
uploaded_files = st.sidebar.file_uploader("Upload PDFs, TXT, or Images", accept_multiple_files=True, type=["pdf", "txt", "png", "jpg", "jpeg", "tiff", "bmp"])

# Session state for storing document chunks and vectorstore
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'all_splits' not in st.session_state:
    st.session_state.all_splits = None

# Temporary directory to hold uploaded files
temp_dir = tempfile.mkdtemp()

# Save uploaded files to temp directory
if uploaded_files:
    st.sidebar.success("Uploaded files:")
    for uploaded_file in uploaded_files:
        st.sidebar.write(f"- {uploaded_file.name}")
        with open(os.path.join(temp_dir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

    # Load and process documents
    with st.spinner("Processing documents and generating embeddings..."):
        all_splits = load_and_process_pdfs(temp_dir)
        vectorstore = initialize_vectorstore(all_splits)
        st.session_state.vectorstore = vectorstore
        st.session_state.all_splits = all_splits
        st.success("Documents processed and stored!")

# Main area
st.subheader("Ask a Question about the Uploaded Documents")
query = st.text_input("Enter your question")

if st.button("Get Answer") and query:
    if st.session_state.vectorstore is None:
        st.warning("Please upload and process documents first.")
    else:
        with st.spinner("Retrieving relevant chunks and generating response..."):
            if query:
                with st.spinner("Fetching response..."):
                 chunks, answer = get_chunks_and_answer(query,  st.session_state.vectorstore)

                 st.subheader("🔍 Retrieved Chunks:")
                 for i, chunk in enumerate(chunks):
                  st.markdown(f"- **Doc ID:** {chunk['doc_id']}")
                  st.markdown(f"- **Text:** {chunk['text']}")
                  st.markdown(f"- **Page Number:** {chunk['page_number']}")
                  st.markdown(f"- **Paragraph Approx:** {chunk['paragraph_approx']}")
                  st.markdown("---")

                st.subheader("💡 Final Answer from LLM:")
                st.markdown(answer)



---

# 📚 Document RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions based on the content of **PDFs, text files, and images**. This application uses **LangChain**, **FAISS**, **Google Gemini LLM**, and **Streamlit** for an interactive Q\&A interface.

---

##  Features

* **Document Ingestion**: Automatically loads `.pdf`, `.txt`, and image files (`.jpg`, `.png`, etc.)
* **Chunking & Storage**: Splits text into overlapping chunks and stores metadata in **SQLite**.
* **Semantic Search**: Retrieves relevant document chunks using **FAISS** and **SentenceTransformers embeddings**.
* **Answer Generation**: Uses **Google Gemini LLM** to generate accurate responses based on retrieved chunks.
* **Streamlit UI**: Clean and simple interface for uploading files and asking questions.

---

## 🛠️ Tech Stack

| Layer        | Library/Tool                                 |
| ------------ | -------------------------------------------- |
| UI           | Streamlit                                    |
| Vector Store | FAISS                                        |
| Embeddings   | Sentence Transformers (`all-MiniLM-L6-v2`)   |
| LLM          | Google Gemini (`gemini-2.0-flash-001`)       |
| OCR          | Tesseract via `pytesseract`                  |
| File Parsing | `PyPDFLoader`, `TextLoader`, `PIL`, `PyPDF2` |
| Database     | SQLite                                       |
| Framework    | LangChain                                    |

---

---

## 💬 How It Works

1. **Preprocessing**:

   * All files are loaded from the `data/` folder.
   * PDF/TXT text is split into chunks.
   * Image files are processed via OCR.
   * Metadata is stored in SQLite.

2. **Semantic Retrieval**:

   * When a query is submitted, relevant chunks are retrieved using FAISS.

3. **LLM Answer Generation**:

   * Retrieved chunks are passed to Gemini to generate a final answer.
   * Both chunks and the answer are shown in the UI.

---


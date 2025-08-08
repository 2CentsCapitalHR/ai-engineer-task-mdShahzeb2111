# Corporate Agent — ADGM Doc Reviewer (MVP)

This repository contains two Streamlit apps for reviewing ADGM-related corporate documents:

- **Classic Rule-Based Reviewer (`app.py` + `reviewer.py`)**  
  Detects document types, checks for required files, highlights legal red flags, and annotates `.docx` files with comments and a structured JSON summary.

- **RAG-Powered Reviewer (`app1.py` + `rag_reviewer.py`)**  
  Uses Retrieval-Augmented Generation (RAG) with an LLM (OpenAI GPT or Gemini) and FAISS to retrieve relevant context from your documents and generate a structured review.

---

## Features

- Upload `.docx` files for review
- Automatic detection of document type (e.g., Articles of Association, UBO Declaration)
- Checklist verification for ADGM processes (e.g., company incorporation)
- Highlights issues such as ambiguous language, missing signatures, and incorrect jurisdiction references
- Annotated `.docx` download for each file (classic version)
- Structured JSON summary of findings
- RAG version: retrieves relevant context and generates a review using an LLM

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

---

## Running the Apps

### Classic Rule-Based Reviewer

```sh
streamlit run app.py
```

### RAG-Powered Reviewer (OpenAI or Gemini)

```sh
streamlit run app1.py
```

---

## Usage

1. **Enter your API key** (for RAG version: OpenAI or Gemini).
2. **Upload one or more `.docx` files**.
3. **Enter your review question/request** (RAG version).
4. **Click the review button**.
5. **View the structured JSON summary and download annotated documents** (classic), or view the retrieved context and AI-generated review (RAG).

---

## Project Structure

```
app.py           # Streamlit UI (classic rule-based)
reviewer.py      # Rule-based document processing logic
app1.py          # Streamlit UI (RAG-powered)
rag_reviewer.py  # RAG logic (embeddings, retrieval, LLM generation)
requirements.txt # Python dependencies
README.md        # This file
```

---

## Requirements

- Python 3.8+
- For RAG: OpenAI API key or Gemini API key (see code comments)
- See `requirements.txt` for all dependencies

---

## Example Output

### Classic

- Structured JSON summary of findings
- Downloadable annotated `.docx` files

### RAG

- Retrieved context (most relevant paragraphs)
- AI-generated review (structured, with suggestions and highlights)

---

## License

MIT License

---

*Built with Streamlit, python-docx, FAISS, OpenAI GPT, Gemini, and sentence-transformers.*

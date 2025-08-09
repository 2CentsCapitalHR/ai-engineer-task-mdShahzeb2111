# Corporate Agent — ADGM Doc Reviewer (RAG-powered MVP)

This Streamlit app reviews ADGM-related corporate documents using Retrieval-Augmented Generation (RAG) with Gemini (Google Generative AI).  
It checks for required documents, highlights legal red flags, and generates a structured review.

## Features

- Upload `.docx` files for review
- Automatic detection of document type
- Checklist verification for ADGM processes (e.g., company incorporation)
- Highlights issues such as ambiguous language, missing signatures, and incorrect jurisdiction references
- Structured JSON summary of findings
- RAG: retrieves relevant context and generates a review using Gemini

## Getting Started

1. Clone the repository  
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app  
   ```sh
   streamlit run app.py
   ```
4. Enter your Gemini API key (get one at [Google AI Studio](https://aistudio.google.com/app/apikey))

## Usage

1. Enter your Gemini API key.
2. Upload one or more `.docx` files.
3. Enter your review question/request.
4. Click "Run RAG Review".
5. View the structured JSON summary, retrieved context, and AI-generated review.
6. Download the review file in  .docx format.
---

*Built with Streamlit, python-docx, FAISS, sentence-transformers, and Gemini.*


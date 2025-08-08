import io
import numpy as np
import faiss
from docx import Document
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Define required document types for incorporation
REQUIRED_DOCS = [
    "Articles of Association",
    "Memorandum of Association",
    "Incorporation Application",
    "UBO Declaration",
    "Register of Members and Directors"
]

DOC_TYPE_KEYWORDS = {
    "Articles of Association": ["articles of association", "aoa"],
    "Memorandum of Association": ["memorandum of association", "moa"],
    "Incorporation Application": ["incorporation application", "application for incorporation"],
    "UBO Declaration": ["ultimate beneficial owner", "ubo", "beneficial owner"],
    "Register of Members and Directors": ["register of members", "register of directors", "members register"],
}

def extract_paragraphs(doc_bytes):
    doc = Document(io.BytesIO(doc_bytes))
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]

def detect_doc_type(text):
    t = text.lower()
    for typ, kws in DOC_TYPE_KEYWORDS.items():
        for kw in kws:
            if kw in t:
                return typ
    return "Unknown"

def build_faiss_index(paragraphs):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(paragraphs)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings.astype('float32'))
    return index, embeddings, model

def retrieve_context(query, paragraphs, index, model, top_k=3):
    q_emb = model.encode([query])
    D, I = index.search(q_emb.astype('float32'), top_k)
    return [paragraphs[i] for i in I[0]]

def generate_review(query, context, api_key):
    genai.configure(api_key=api_key)
    prompt = (
        "You are an expert legal reviewer for ADGM documents. "
        "Given the following context from a document:\n\n"
        + "\n\n".join(context) +
        f"\n\nUser question/request: {query}\n\n"
        "For each issue, cite the exact ADGM law or rule that applies. "
        "If a required document is missing, mention it. "
        "Provide a structured review, highlight issues, and suggest improvements."
    )
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

def process_files_with_rag(files, user_query, api_key):
    # Analyze all files, detect types, and build a checklist
    doc_types = []
    doc_names = []
    all_paragraphs = []
    file_paragraphs = []
    for uploaded_file in files:
        content = uploaded_file.read()
        paragraphs = extract_paragraphs(content)
        all_paragraphs.extend(paragraphs)
        file_paragraphs.append((uploaded_file.name, paragraphs))
        # Detect doc type from first 1000 chars
        doc_text = " ".join(paragraphs)[:1000]
        doc_type = detect_doc_type(doc_text)
        doc_types.append(doc_type)
        doc_names.append(uploaded_file.name)
    # Checklist logic
    found = [d for d in doc_types if d in REQUIRED_DOCS]
    missing = [d for d in REQUIRED_DOCS if d not in found]
    # Retrieval
    index, embeddings, model = build_faiss_index(all_paragraphs)
    context = retrieve_context(user_query, all_paragraphs, index, model)
    review = generate_review(user_query, context, api_key)
    # Structured output
    summary = {
        "process": "Company Incorporation",
        "documents_uploaded": len(files),
        "detected_document_types": doc_types,
        "required_documents": REQUIRED_DOCS,
        "documents_found": len(found),
        "missing_documents": missing,
        "file_names": doc_names,
        "issues_found": review
    }
    return summary, review, context

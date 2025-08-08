import io
import numpy as np
import faiss
import openai
from docx import Document

def extract_paragraphs(doc_bytes):
    doc = Document(io.BytesIO(doc_bytes))
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]

def get_openai_embedding(text, api_key):
    openai.api_key = api_key
    response = openai.Embedding.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

def build_faiss_index(paragraphs, api_key):
    embeddings = [get_openai_embedding(p, api_key) for p in paragraphs]
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index, embeddings

def retrieve_context(query, paragraphs, index, api_key, top_k=3):
    q_emb = get_openai_embedding(query, api_key)
    D, I = index.search(np.array([q_emb]).astype('float32'), top_k)
    return [paragraphs[i] for i in I[0]]

def generate_review(query, context, api_key):
    prompt = (
        "You are an expert legal reviewer for ADGM documents. "
        "Given the following context from a document:\n\n"
        + "\n\n".join(context) +
        f"\n\nUser question/request: {query}\n\n"
        "Provide a structured review, highlight issues, and suggest improvements."
    )
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content

def process_docx_with_rag(doc_bytes, user_query, api_key):
    paragraphs = extract_paragraphs(doc_bytes)
    index, _ = build_faiss_index(paragraphs, api_key)
    context = retrieve_context(user_query, paragraphs, index, api_key)
    review = generate_review(user_query, context, api_key)
    return review, context
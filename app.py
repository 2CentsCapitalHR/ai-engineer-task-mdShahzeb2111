import streamlit as st
from rag_reviewer import process_files_with_rag

st.title("Corporate Agent — ADGM Doc Reviewer (RAG-powered MVP)")
st.write("Upload your ADGM-related `.docx` documents for review. The agent will check for completeness, highlight red flags, and generate a structured review using Gemini (Google Generative AI).")

api_key = st.text_input("Enter your Gemini API Key", type="password")
uploaded_files = st.file_uploader("Upload .docx files", type=["docx"], accept_multiple_files=True)
user_query = st.text_area("Enter your review question/request", value="Review these documents for ADGM compliance and highlight any issues.")

if uploaded_files and api_key and user_query:
    if st.button("Run RAG Review"):
        with st.spinner("Processing..."):
            summary, review, context = process_files_with_rag(uploaded_files, user_query, api_key)
        st.subheader("Structured JSON Summary")
        st.code(summary, language="json")
        st.subheader("Retrieved Context")
        for c in context:
            st.write(f"- {c}")
        st.subheader("AI-Generated Review")
        st.write(review)

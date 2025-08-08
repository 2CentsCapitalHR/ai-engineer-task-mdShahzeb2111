import streamlit as st
from rag_reviewer import process_docx_with_rag

st.title("RAG-powered ADGM Doc Reviewer (MVP)")
st.write("Upload a `.docx` file and enter your review question/request. The app will retrieve relevant context and generate a review using OpenAI GPT.")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
uploaded_file = st.file_uploader("Upload a .docx file", type=["docx"])
user_query = st.text_area("Enter your review question/request", value="Review this document for ADGM compliance and highlight any issues.")

if uploaded_file and api_key and user_query:
    if st.button("Run RAG Review"):
        with st.spinner("Processing..."):
            review, context = process_docx_with_rag(uploaded_file.read(), user_query, api_key)
        st.subheader("Retrieved Context")
        for c in context:
            st.write(f"- {c}")
        st.subheader("AI-Generated Review")
        st.write(review)
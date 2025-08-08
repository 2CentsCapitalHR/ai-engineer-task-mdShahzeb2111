import streamlit as st
from reviewer import process_files

st.title("Corporate Agent — ADGM doc reviewer (MVP)")
st.write("Upload one or more .docx files for review.")

uploaded_files = st.file_uploader("Upload .docx files", type=["docx"], accept_multiple_files=True)

if uploaded_files:
    if st.button("Review documents"):
        summary, annotated_files = process_files(uploaded_files)
        st.subheader("Structured JSON Summary")
        st.code(summary, language="json")
        st.subheader("Download reviewed document(s)")
        for name, b in annotated_files:
            st.download_button(
                label=f"Download {name}",
                data=b,
                file_name=name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
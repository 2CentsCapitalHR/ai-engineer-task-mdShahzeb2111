# Corporate Agent — ADGM Doc Reviewer (MVP)

This is a Streamlit app for reviewing ADGM-related corporate documents. It allows you to upload `.docx` files, automatically detects document types, highlights issues, and provides annotated downloads and a structured JSON summary.

## Features

- Upload one or more `.docx` files for review
- Automatic detection of document type (e.g., Articles of Association, UBO Declaration)
- Highlights issues such as ambiguous language, missing signatures, and incorrect jurisdiction references
- Annotated `.docx` download for each file
- Structured JSON summary of findings

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

### 3. Run the app

```sh
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Structure

```
app.py           # Streamlit UI
reviewer.py      # Document processing logic
requirements.txt # Python dependencies
README.md        # This file
```

## Usage

1. Click "Browse files" to upload one or more `.docx` files.
2. Click "Review documents".
3. View the structured JSON summary.
4. Download the reviewed/annotated documents.

## License

MIT License

---

*Built with Streamlit
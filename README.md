# RAG-Project-1

A Retrieval-Augmented Generation (RAG) application built with Streamlit that allows users to upload documents and ask questions based on their content. The application retrieves relevant document chunks using FAISS and generates answers using Google's Gemini API.

## Features

- Upload PDF, DOCX, TXT, and PPTX documents
- Ask questions about the uploaded document
- Retrieval-Augmented Generation (RAG) using FAISS
- Multi-language response support
- Text-to-Speech for generated answers
- Display retrieved document chunks for transparency
- Chat-style interface with conversation history
- Local document processing

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Google Gemini API
- gTTS
- Sentence Transformers

## Project Structure

```
RAG-Project-1/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── src/
│   ├── document_loader.py
│   ├── embedding.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── text_splitter.py
│   ├── text_to_speech.py
│   └── vector_store.py
│
└── uploads/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yashpratapsinghthakur/RAG-Project-1.git
```

Move into the project directory:

```bash
cd RAG-Project-1
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain a Gemini API key from Google AI Studio.

## Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

## How It Works

1. Upload a supported document.
2. The document is loaded and split into smaller chunks.
3. Embeddings are created for each chunk.
4. FAISS indexes the embeddings.
5. When a question is asked, the most relevant chunks are retrieved.
6. Gemini generates an answer using the retrieved context.
7. The answer can also be converted to speech.

## Supported File Types

- PDF
- DOCX
- TXT
- PPTX

## Future Improvements

- Support for multiple uploaded documents
- Better citation and source references
- Chat history export
- Voice input
- Improved document preview
- Authentication and user management

## Usage Restriction

This repository is shared for portfolio and educational purposes only.

You may view the source code, but you may not copy, reuse, modify, redistribute, or use any part of this project in your own work without prior written permission from the author.

© 2026 Yash Pratap Singh Thakur. All rights reserved.

---

## Author

**Yash Pratap Singh Thakur**

import os
import streamlit as st

from src.document_loader import load_document
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.rag_pipeline import ask_rag
from src.text_to_speech import text_to_speech

st.set_page_config(
    page_title=" Local RAG Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Local RAG Assistant")

# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "docs" not in st.session_state:
    st.session_state.docs = None

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙ Settings")

language = st.sidebar.selectbox(
    "Answer Language",
    [
        "Auto",
        "English",
        "Hindi",
        "French",
        "German",
        "Spanish",
        "Japanese",
        "Chinese",
    ],
)

show_chunks = st.sidebar.checkbox(
    "Show Retrieved Chunks",
    value=True,
)

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()

# ---------------- UPLOAD ---------------- #

os.makedirs("uploads", exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "docx", "txt", "pptx"],
)

if uploaded_file:

    file_path = os.path.join(
        "uploads",
        uploaded_file.name,
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if (
        st.session_state.vector_store is None
        or st.session_state.current_file != uploaded_file.name
    ):

        with st.spinner("Indexing document..."):

            docs = load_document(file_path)

            chunks = split_documents(docs)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store
            st.session_state.docs = docs
            st.session_state.current_file = uploaded_file.name

    st.success("✅ Document indexed successfully!")

    with st.expander("📄 Document Preview"):

        st.text(
            st.session_state.docs[0].page_content[:3000]
        )

    # ---------------- CHAT HISTORY ---------------- #

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if (
                message["role"] == "assistant"
                and "audio" in message
            ):

                st.audio(
                    message["audio"],
                    format="audio/mp3",
                )
        # ---------------- CHAT INPUT ---------------- #

    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Retrieve relevant chunks
        retrieved_docs = retrieve_documents(
            st.session_state.vector_store,
            question,
        )

        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner("🤖 Thinking..."):

                answer = ask_rag(
                    st.session_state.vector_store,
                    question,
                    language,
                )

            st.markdown(answer)

            # Show retrieved chunks
            if show_chunks:

                with st.expander("📚 Retrieved Chunks"):

                    for i, doc in enumerate(
                        retrieved_docs,
                        start=1,
                    ):

                        st.markdown(f"### Chunk {i}")
                        st.write(doc.page_content)
                        st.divider()

            # ---------- TEXT TO SPEECH ---------- #

            language_map = {
                "Auto": "en",
                "English": "en",
                "Hindi": "hi",
                "French": "fr",
                "German": "de",
                "Spanish": "es",
                "Japanese": "ja",
                "Chinese": "zh-cn",
            }

            audio_path = text_to_speech(
                answer,
                language_map.get(language, "en"),
            )

            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()

            st.audio(
                audio_bytes,
                format="audio/mp3",
            )

            # ---------- DOWNLOAD BUTTON ---------- #

            st.download_button(
                "⬇ Download Answer",
                answer,
                file_name="answer.txt",
                mime="text/plain",
            )

        # Save assistant response in chat history
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "audio": audio_bytes,
            }
        )  
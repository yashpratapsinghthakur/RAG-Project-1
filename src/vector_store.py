from langchain_community.vectorstores import FAISS

from src.embedding import get_embedding_model


def create_vector_store(chunks):
    """
    Create a FAISS vector database from document chunks.
    """

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    return vector_store
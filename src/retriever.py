def retrieve_documents(vector_store, query: str, k: int = 3):
    """
    Retrieve the most relevant document chunks.

    Args:
        vector_store: FAISS vector store.
        query: User's question.
        k: Number of chunks to retrieve.

    Returns:
        List of relevant document chunks.
    """

    return vector_store.similarity_search(
        query=query,
        k=k,
    )
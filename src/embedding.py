from langchain_ollama import OllamaEmbeddings

EMBEDDING_MODEL = "nomic-embed-text"


def get_embedding_model():
    """
    Return the Ollama embedding model.
    """

    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
    )
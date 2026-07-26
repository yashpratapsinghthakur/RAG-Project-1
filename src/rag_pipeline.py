from src.retriever import retrieve_documents
from src.llm import generate_response


def ask_rag(vector_store, query, language="Auto"):

    docs = retrieve_documents(
        vector_store,
        query,
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    if language == "Auto":

        language_instruction = (
            "Reply in the SAME language as the user's question."
        )

    else:

        language_instruction = (
            f"Reply ONLY in {language}."
        )

    prompt = f"""
You are an intelligent multilingual RAG assistant.

Answer ONLY using the provided context.

Do NOT make up information.

{language_instruction}

If the answer is not present in the context, reply exactly:

"I don't know based on the provided document."

------------------------
Context:
{context}
------------------------

Question:
{query}

Answer:
"""

    return generate_response(prompt)
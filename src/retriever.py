from langchain_community.vectorstores import FAISS

from src.embeddings import get_embeddings
from src.config import VECTOR_DB_DIR


def load_vector_store():
    """
    Load the saved FAISS vector database.
    """

    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        str(VECTOR_DB_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def get_retriever():

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    question = "How can I reset my password?"

    docs = retriever.invoke(question)

    print("=" * 60)

    print(f"Retrieved Documents: {len(docs)}")

    print("=" * 60)

    for i, doc in enumerate(docs):
        print(f"\nDocument {i+1}\n")
        print(doc.page_content)
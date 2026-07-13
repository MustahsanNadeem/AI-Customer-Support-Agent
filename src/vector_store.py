from langchain_community.vectorstores import FAISS

from src.text_splitter import split_documents
from src.embeddings import get_embeddings

from src.config import VECTOR_DB_DIR


def create_vector_store():
    """
    Create and save the FAISS vector database.
    """

    print("Loading document chunks...")

    documents = split_documents()

    print(f"Total Chunks: {len(documents)}")

    print("Loading embedding model...")

    embeddings = get_embeddings()

    print("Creating FAISS vector database...")

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    print("Saving vector database...")

    # Create vector_db folder if it doesn't exist
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

    vector_store.save_local(str(VECTOR_DB_DIR))

    print("Vector Database Saved Successfully!")

    return vector_store


if __name__ == "__main__":
    create_vector_store()
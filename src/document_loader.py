from langchain_community.document_loaders import TextLoader
from config import KNOWLEDGE_FILE


def load_documents():
    """
    Load customer support knowledge base.
    """

    try:
        loader = TextLoader(
            file_path=str(KNOWLEDGE_FILE),
            encoding="utf-8"
        )

        documents = loader.load()

        return documents

    except Exception as e:
        print(f"Error loading documents: {e}")
        return []
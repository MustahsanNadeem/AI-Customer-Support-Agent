from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    UnstructuredMarkdownLoader,
    Docx2txtLoader,
)

from src.config import DATA_DIR


def load_documents():

    documents = []

    for file in Path(DATA_DIR).iterdir():

        suffix = file.suffix.lower()

        try:

            if suffix == ".txt":
                loader = TextLoader(str(file), encoding="utf-8")

            elif suffix == ".pdf":
                loader = PyPDFLoader(str(file))

            elif suffix == ".csv":
                loader = CSVLoader(str(file))

            elif suffix == ".docx":
                loader = Docx2txtLoader(str(file))

            elif suffix == ".md":
                loader = UnstructuredMarkdownLoader(str(file))

            else:
                continue

            documents.extend(loader.load())

        except Exception as e:

            print(f"Error loading {file.name}: {e}")

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(f"\nLoaded {len(docs)} documents.\n")

    for doc in docs:

        print(doc.metadata)
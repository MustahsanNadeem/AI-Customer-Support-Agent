from src.document_loader import load_documents
from src.config import CHUNK_SIZE, CHUNK_OVERLAP

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents():

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


if __name__ == "__main__":

    chunks = split_documents()

    print("=" * 60)
    print(f"Total Chunks: {len(chunks)}")
    print("=" * 60)

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}\n")
        print(chunk.page_content)
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL


def get_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    return embeddings


if __name__ == "__main__":
    embedding_model = get_embeddings()

    vector = embedding_model.embed_query("How can I reset my password?")

    print(f"Vector Length: {len(vector)}")
    print(vector[:10])
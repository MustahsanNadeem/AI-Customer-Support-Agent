from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
    )
    return llm


if __name__ == "__main__":
    api_key = os.getenv("OPENROUTER_API_KEY")
    print("API Key Loaded:", api_key[:15] + "...")

    llm = get_llm()

    response = llm.invoke("Introduce yourself in one sentence.")

    print("\nResponse:")
    print(response.content)
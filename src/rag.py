from pathlib import Path

from src.prompts import CHATBOT_PROMPT
from src.retriever import get_retriever
from src.llm import get_llm
from src.memory import memory


retriever = get_retriever()
llm = get_llm()


def ask(question):

    # Load previous conversation
    history_messages = memory.load_memory_variables({})["chat_history"]

    history = "\n".join(
        [
            f"{msg.type}: {msg.content}"
            for msg in history_messages
        ]
    )

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Build prompt
    prompt = CHATBOT_PROMPT.format(
        history=history,
        context=context,
        question=question
    )

    # Get LLM response
    response = llm.invoke(prompt)

    # Save conversation
    memory.save_context(
        {"input": question},
        {"output": response.content}
    )

    # Collect source files
    sources = []

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")

        filename = Path(source).name

        if filename not in sources:
            sources.append(filename)

    return response.content, sources


if __name__ == "__main__":

    question = input("Ask: ")

    answer, sources = ask(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:")

    for source in sources:
        print("-", source)
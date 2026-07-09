from langchain_core.prompts import ChatPromptTemplate


def get_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert AI Assistant.

Rules:

1. Answer ONLY from the provided context.

2. If the answer is not available in the context, reply:

"I don't have enough information to answer that."

3. Never make up information.

4. Give clear, professional and structured answers.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt


if __name__ == "__main__":

    prompt = get_prompt()

    print(prompt)
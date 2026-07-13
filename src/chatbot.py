from rag import ask

print("=" * 60)
print("AI Customer Support Agent")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer, sources = ask(question)

    print("\nBot:\n")
    print(answer)

    print("\nSources:")

    for source in sources:
        print("-", source)
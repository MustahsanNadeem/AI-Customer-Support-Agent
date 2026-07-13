import streamlit as st

from src.rag import ask


st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Customer Support Agent")

st.write("Ask any question about our products or services.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("Type your question...")


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, sources = ask(question)

        st.markdown(answer)

        st.markdown("---")

        st.markdown("**Sources**")

        for source in sources:
            st.write(f"📄 {source}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
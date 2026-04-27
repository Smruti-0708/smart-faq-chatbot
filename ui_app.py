import streamlit as st
import ollama

st.title("🎓 Smart FAQ Chatbot")

syllabus = """
Course: Artificial Intelligence

Modules:
1. Introduction to AI
2. Machine Learning Basics
3. Neural Networks
4. Natural Language Processing
5. Computer Vision
"""

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": f"""
You are a strict college FAQ chatbot.

Use ONLY this syllabus:

{syllabus}

Rules:
- Only syllabus questions
- Bullet points
- Max 5 points
"""
        }
    ]

# Input
question = st.text_input("Ask your question:")

if st.button("Get Answer"):

    if not question.strip():
        st.warning("Enter a valid question")
    else:
        try:
            st.session_state.messages.append({"role": "user", "content": question})

            response = ollama.chat(
                model="tinyllama",
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]

            st.session_state.messages.append({"role": "assistant", "content": answer})

            st.success(answer)

        except Exception as e:
            st.error("⚠️ Error: Make sure Ollama is running (ollama run tinyllama)")
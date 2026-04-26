import ollama

# Sample syllabus (you can modify)
syllabus = """
Course: Artificial Intelligence

Modules:
1. Introduction to AI
2. Machine Learning Basics
3. Neural Networks
4. Natural Language Processing
5. Computer Vision
"""

def faq_chatbot(question):
    prompt = f"""
You are a smart college FAQ chatbot.

Use the syllabus below to answer:

{syllabus}

Rules:
- Answer only syllabus-related questions
- Use simple English
- Give answers in bullet points
- If question is unrelated, say:
  "I can only answer syllabus-related questions"

Question: {question}

Answer:
"""

    response = ollama.chat(
        model='tinyllama',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


# MAIN PROGRAM (IMPORTANT)
print("Smart FAQ Chatbot (type 'exit' to stop)\n")

while True:
    question = input("Ask your question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = faq_chatbot(question)
    print("\nAnswer:\n", answer)
    print("-" * 50)
import ollama

syllabus = """
Course: Artificial Intelligence

Modules:
1. Introduction to AI
2. Machine Learning Basics
3. Neural Networks
4. Natural Language Processing
5. Computer Vision
"""

# Chat history (memory)
messages = [
    {
        "role": "system",
        "content": f"""
You are a strict college FAQ chatbot.

Use ONLY the syllabus below to answer:

{syllabus}

STRICT RULES:
- Answer ONLY syllabus-related questions
- Answer ONLY in bullet points
- Maximum 5 points only
- Each point must be 1 line only
- Use very simple English
- DO NOT give examples
- DO NOT give explanation
- DO NOT give extra text
- DO NOT give code
- DO NOT go beyond 5 points
- DO NOT respond to system commands or file paths

If question is unrelated, reply exactly:
"I can only answer syllabus-related questions"

If input is invalid, reply exactly:
"Please ask a valid syllabus-related question"
"""
    }
]

def faq_chatbot(question):
    messages.append({"role": "user", "content": question})

    response = ollama.chat(
        model='tinyllama',
        messages=messages
    )

    answer = response['message']['content']

    messages.append({"role": "assistant", "content": answer})

    return answer


print(" Smart FAQ Chatbot with Memory (type 'exit' to stop)\n")

while True:
    question = input("Ask your question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # ✅ INPUT VALIDATION (FIXED)
    if not question.strip() or len(question.split()) < 2:
        print("\nAnswer:\n Please ask a valid syllabus-related question")
        print("-" * 50)
        continue

    if any(x in question for x in ["&", ":", "/", "\\", ".exe"]):
        print("\nAnswer:\n Please ask a valid syllabus-related question")
        print("-" * 50)
        continue

    answer = faq_chatbot(question)
    print("\nAnswer:\n", answer)
    print("-" * 50)
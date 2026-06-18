import spacy

nlp = spacy.load("en_core_web_sm")

IPC = {
    "302": "Section 302 IPC: Punishment for murder.",
    "375": "Section 375 IPC: Rape definition under Indian law.",
    "376": "Section 376 IPC: Punishment for rape.",
    "420": "Section 420 IPC: Cheating and dishonestly inducing delivery of property.",
    "124a": "Section 124A IPC: Sedition against Government."
}

def get_sec(text):
    for t in nlp(text):
        if t.text.lower() in IPC:
            return t.text.lower()

print("IPC Chatbot: Hello! Ask me about any section of the Indian Penal Code.")

while True:

    q = input("You: ").lower()
    if q in ["exit", "quit", "bye"]:
        print("IPC Chatbot: Goodbye!")
        break

    elif "hi" in q or "hello" in q:
        print("IPC Chatbot: Hello! Ask me about any IPC section.")

    else:
        s = get_sec(q)

        if s:
            print(f"IPC Chatbot: {IPC[s]}")
        else:
            print("IPC Chatbot: I can help you with information about the Indian Penal Code. Try asking about a section like 'What is Section 420?'")
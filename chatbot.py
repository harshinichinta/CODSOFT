def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("ChatBot: Hello! How can I help you?")

        elif "your name" in user:
            print("ChatBot: My name is CodSoft ChatBot.")

        elif "how are you" in user:
            print("ChatBot: I am fine. Thank you!")

        elif "ai" in user:
            print("ChatBot: AI stands for Artificial Intelligence.")

        elif "python" in user:
            print("ChatBot: Python is a popular programming language.")

        elif user == "bye":
            print("ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")
chatbot()
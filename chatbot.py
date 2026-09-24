def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or "hi" :
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what are you doing":
             print("Chatbot: Chatting with you!")

        elif user_input == "what is your name":
            print("Chatbot: My name is SimpleBot.")

        elif user_input == "help":
            print("Chatbot: Sure! You can say hello, ask how I am, or say bye.")

        elif user_input == "thank you":
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
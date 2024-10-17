def main():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

def get_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "what is your name?": "I'm a chatbot created to assist you.",
        "how are you?": "I'm just a bunch of code, but thanks for asking!"
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    main()

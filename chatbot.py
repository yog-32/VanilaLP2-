import random

# Responses for greeting
GREETINGS = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
INTRODUCTION = "I'm your friendly catboat assistant. How can I help you today?"

# Responses for different types of queries
QUERY_RESPONSES = {
    "products": ["We offer a wide range of products. What are you looking for?", 
                 "Our products include electronics, clothing, accessories, and more. How can I assist you?"],
    "services": ["We provide various services such as shipping, returns, and customer support. What do you need help with?",
                 "Our services include fast shipping, easy returns, and 24/7 customer support. How can I assist you?"],
    "policies": ["Our policies cover returns, refunds, privacy, and more. What policy information do you need?",
                 "You can find information about our policies regarding returns, refunds, and privacy on our website. Anything specific you'd like to know?"],
    "contact": ["You can contact us via phone, email, or live chat. How would you like to reach us?",
                "Our customer support team is available 24/7 to assist you. How can we assist you?"],
    "default": ["I'm sorry, I'm not sure how to help with that. Can you please provide more details?",
                "I'm not familiar with that request. Could you please try asking in a different way?"]
}

# Responses for task assistance
TASK_ASSISTANCE = ["Sure, I can assist you with that.", "Of course, I'm here to help."]

# Responses for closing interaction
GOODBYE = ["Thank you for using our catboat assistant. Have a great day!", "Goodbye! Don't hesitate to come back if you need assistance."]

def greet_user():
    print(random.choice(GREETINGS))
    print(INTRODUCTION)

def handle_query(query):
    if "product" in query:
        print(random.choice(QUERY_RESPONSES["products"]))
    elif "service" in query:
        print(random.choice(QUERY_RESPONSES["services"]))
    elif "policy" in query:
        print(random.choice(QUERY_RESPONSES["policies"]))
    elif "contact" in query:
        print(random.choice(QUERY_RESPONSES["contact"]))
    else:
        print(random.choice(QUERY_RESPONSES["default"]))

def assist_with_task():
    print(random.choice(TASK_ASSISTANCE))

def say_goodbye():
    print(random.choice(GOODBYE))

# Main interaction loop
def main():
    greet_user()

    while True:
        user_input = input("User: ").strip().lower()

        if user_input == "exit":
            break

        handle_query(user_input)
        assist_with_task()

    say_goodbye()

if __name__ == "__main__":
    main()

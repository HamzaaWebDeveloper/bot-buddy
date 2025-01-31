import nltk 
from nltk.chat.util import Chat, reflections


nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! 👋", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great!", "All systems go! 😊"]
    ],
    [
        r"what is your name?",
        ["I'm your first chatbot! Call me BotBuddy.", "I'm PythonBot! 🐍"]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! 👋", "See you later!"]
    ],
    [
        r"(.*)",
        ["I’m still learning! Can you rephrase that?", "Hmm, I don’t understand yet. Try asking something else."]
    ]
]

chatbot = Chat(pairs,reflections) 


print("ChatBot: Hi! I'm your first chatbot, type 'quit' to exit.")

while True :
    user_input = input("You:")
    if user_input.lower() == 'quit':
        print ("ChatBot: GoodBye")
        break
    response = chatbot.respond(user_input)

    print("ChatBot : " , response)
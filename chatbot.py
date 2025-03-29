from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    "SupportBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbot.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm sorry, I don't understand. Can you rephrase?",
            "maximum_similarity_threshold": 0.8
        }
    ]
)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")

list_trainer = ListTrainer(chatbot)
list_trainer.train([
    "Hello",
    "Hi there! How can I assist you?",
    "What is your name?",
    "I am SupportBot, your virtual assistant.",
    "How do I reset my password?",
    "You can reset your password by clicking 'Forgot Password' on the login page."
])

print("Chatbot training completed!")

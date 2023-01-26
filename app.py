from flask import Flask, request, jsonify
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('Coffee Bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

@app.route('/process-input', methods=['POST'])
def process_input():
    user_input = request.json['input']
    response = chatbot.get_response(user_input)
    return jsonify(response=str(response))

if __name__ == '__main__':
    app.run(debug=True)

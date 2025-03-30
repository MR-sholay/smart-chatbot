from flask import Flask, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Smart Chatbot API!"

@app.route("/chat", methods=["POST"])
def chat():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.json
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Simple chatbot logic
    if "farming" in user_input.lower():
        reply = "Use quality seeds and proper irrigation for better farming."
    elif "health" in user_input.lower():
        reply = "Please visit a nearby health center or doctor."
    elif "scheme" in user_input.lower():
        reply = "Check government schemes on official websites like PM Yojana."
    else:
        reply = "I can help with agriculture, healthcare, and government schemes."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

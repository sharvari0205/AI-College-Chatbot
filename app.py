from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

college_info = {
    "admission": "Admissions are open as per the college schedule.",
    "courses": "We offer undergraduate and postgraduate courses.",
    "fees": "Please contact the college office for fee details.",
    "timing": "College timings are generally 9 AM to 4 PM.",
    "exam": "Please check the official notice board for exam dates.",
    "library": "The library is available to registered students.",
    "contact": "Please contact the college office for assistance."
}

def chatbot_response(message):
    message = message.lower()

    for keyword, response in college_info.items():
        if keyword in message:
            return response

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to the College Chatbot."

    if "thank" in message:
        return "You're welcome! Happy to help."

    return (
        "Sorry, I couldn't understand your question. "
        "Please contact the college office for more information."
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a question."})

    reply = chatbot_response(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
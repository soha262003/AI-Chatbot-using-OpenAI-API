from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "your_api_key"

def chatbot_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        reply = chatbot_response(user_input)
    return render_template("main.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)

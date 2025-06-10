import webbrowser
from threading import Timer
from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get("msg")
    bot_reply = get_response(user_msg)
    return bot_reply

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run()
from flask import Flask, render_template, redirect, request, flash, url_for, session 

from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

# TODO: remove user that logged out
# Global variables
active_user_list = ['momo']  # nicknames currently active and taken
active_chatrooms = []
messages = []  # TODO: maybe should be a dict?

@app.route("/")
def index():
    """
    This is the main functionality for the site. if logged in,
    the chat will appear in this route.
    """
    return render_template("chatroom.html")

@app.route("/login", methods=["POST","GET"])
def login():
    """
    Login route. if the user hasn't initiated a session, the login "landing page" will be displayed,
    asking for a username and a chat
    """
    if request.method == "POST":
        user_to_register = request.form.get("username")
        if user_to_register in active_user_list:
            flash("sorry, nickname already taken!")
            return redirect(url_for('login'))
        else:
            active_user_list.append(user_to_register)
            session['username'] = user_to_register
            return redirect(url_for('chat_selection'))
    return render_template("landing_page.html")

@app.route("/select_chat", methods=["POST","GET"])
def chat_selection():
    return render_template("chat_selection_page.html", rooms=active_chatrooms)

@socketio.on("submit message")
def vote(data):
    selection = data["selection"]
    # TODO: add message to global variables
    emit("all messages", messages, broadcast=True)

if __name__ == "__main__":
    app.debug = True
    app.env = 'development'
    app.run()

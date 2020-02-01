import os

from flask import Flask, render_template, redirect,request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    """
    This is the main functionality for the site. if logged in, the chat will appear in
    this route.
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
        # TODO: verify that username isn't taken
    # TODO: add session handling for returning client
    return render_template("landing_page.html")

#   @socketio.on()

if __name__ == "__main__":
    app.debug = True
    app.run()
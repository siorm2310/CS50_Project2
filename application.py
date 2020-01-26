import os

from flask import Flask,render_template
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

@app.route("/login")
def login():
    """
    Login route. if the user hasn't initiated a session, the login "landing page" will be displayed,
    asking for a username and a chat
    """
    # TODO: add session handling for returning client
    return render_template("landing_page.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
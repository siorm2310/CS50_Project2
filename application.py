from flask import Flask, render_template, redirect, request, flash, url_for, session 

from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

# TODO: remove user that has logged out
# Global variables
active_user_list = ['momo']  # nicknames currently active and taken
active_chatrooms = {"rooms": [{"name" : "TestRoom1", 
                                "disc" : "BlaBlaBla",
                                "messages" : {"author" : "user", "content": "wow", "time_stamp" : "now"}}]}
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
    if request.method == "POST": # user clicked "Create new chatroom"
        print('got creation reuqest')
        new_chatroom_name = request.form.get("newChatName")
        new_chatroom_disc = request.form.get("newChatDisc")
        active_chatrooms["rooms"].append({"name" : new_chatroom_name , "disc" : new_chatroom_disc})
        return(redirect(url_for('display_chat', chat_name = new_chatroom_name)))
    
    return render_template("chat_selection_page.html", rooms = active_chatrooms["rooms"])

@app.route('/room/<string:chat_name>', methods=["POST","GET"])
def display_chat(chat_name):
    try:
        for room in active_chatrooms["rooms"]:
            if chat_name in room["name"]:
                return render_template("chatroom.html", room = room)
        raise KeyError("Room was not found in active_chatrooms")
    except KeyError as err:
        print(err)
        flash("Room was not found. Choose one of available rooms")
        return redirect(url_for("chat_selection"))


@socketio.on("submit message")
def vote(data):
    selection = data["selection"]
    # TODO: add message to global variables
    emit("all messages", messages, broadcast=True)

if __name__ == "__main__":
    app.debug = True
    app.env = 'development'
    app.run()

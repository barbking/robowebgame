from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from robogameweb import robogame
import secret_settings

app = Flask(__name__)

@app.route("/")
def index():
    # set up session with start value
    session['room_name'] = robogame.START
    print("In index with Room name:", robogame.START)
    return redirect(url_for('game'))

@app.route("/game", methods=['GET','POST'])
def game():
    room_name = session.get('room_name')
    print("in game() with room:", room_name)
    if request.method == 'GET':
        if room_name:
            room = robogame.load_room(room_name)
            print("Room name", room.name)
            return render_template("show_room.html", room=room)
        else:
            return render_template('you_died.html')
    else:
        action = request.form.get('action')
        print("action submitted:", action)

        if room_name and action:
            room = robogame.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room name'] = robogame.name_room(room)
            else:
                session['room_name'] = robogame.name_room(next_room)
        return redirect(url_for('game'))

    # change this if put on the internet
app.secret_key = secret_settings.SECRET_KEY

if __name__ == '__main__':
    app.run()


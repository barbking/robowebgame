from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from robogameweb import robogame


app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    # set up session with start value
    session['room_name'] = robogame.START
    return redirect(url_for('game'))

@app.route("/game", methods=['GET','POST'])
def game():
    room_name = session.get('room_name')
    # check if getting another room, if not end game
    if request.method == 'GET':
        if room_name:
            room = robogame.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template('you_died.html')
    else:
        # if action(input) to do something, go to next room
        action = request.form.get('action')

        if room_name and action:
            room = robogame.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room name'] = robogame.name_room(room)
            else:
                session['room_name'] = robogame.name_room(next_room)
        return redirect(url_for('game'))

# keep secret keys secret, added to config file and gitignore config
app.secret_key = app.config["SECRET_KEY"]


if __name__ == '__main__':
    app.run()


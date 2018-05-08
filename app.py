from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from robogameweb import robogame
import secret_settings
import boto

app = Flask(__name__)

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

# keep secret keys in gitignore, for local deployment uncomment next line
app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

# for heroku deployment
# from boto.s3.connection import S3Connection
# s3 = S3Connection(os.environ['S3_KEY'])

if __name__ == '__main__':
    app.run()


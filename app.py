from flask import Flask, render_template, redirect, url_for
from models import db, Participant
from pony.orm import *
import seed_db
import webbrowser


seed_db.main()
app = Flask(__name__)
db.bind('sqlite', 'participants.db', create_db=True)
db.generate_mapping(create_tables=True)


@app.route('/')
@db_session
def index():
    participants = Participant.select()
    return render_template('index.html', participants=participants)


@app.route('/<name>')
@db_session
def result(name):
    try:
        participant = Participant.get(name=name.title())
        return render_template('result.html', name=participant.name, giving_to=participant.giving_to)
    except:
        return redirect(url_for('index'))


@app.route('/results')
@db_session
def results():
    participants = Participant.select()
    return render_template('results.html', participants=participants)


if __name__ == '__main__':
    webbrowser.open('http://localhost:5000/')
    app.run()


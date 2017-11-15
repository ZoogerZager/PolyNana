from flask import Flask, render_template, redirect, url_for
from models import db, Participant
import run_drawing
import webbrowser


run_drawing.main()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
db.init_app(app)

@app.route('/')
def index():
    participants = Participant.query.all()
    return render_template('index.html', participants=participants)


@app.route('/<name>')
def result(name):
    try:
        participant = Participant.query.filter(Participant.name==name.title()).first_or_404()
        return render_template('result.html', name=participant.name, giving_to=participant.giving_to)
    except:
        return redirect(url_for('index'))


@app.route('/results')
def results():
    participants = Participant.query.all()
    return render_template('results.html', participants=participants)

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000/")
    app.run()


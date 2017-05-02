from flask import Flask
from flask import render_template
import polynanna


app = Flask(__name__)

@app.route('/')
def polyapp():
    return str([p.giving_to for p in polyanna.participants])

@app.route('/<name>')
def result(name=None):
    giving_to = polyanna.get_participant_by_name(name).pop().giving_to
    return render_template('participant.html', name=name, giving_to=giving_to)

if __name__ == '__main__':
    polyanna = polynanna.main()
    app.run()

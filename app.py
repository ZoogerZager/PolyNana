from flask import Flask
from flask import render_template
import polynanna


app = Flask(__name__)

@app.route('/')
def polyapp():
    return render_template('index.html', polyanna=polyanna)

@app.route('/<name>')
def result(name=None):
    giving_to = polyanna.get_participant_by_name(name).giving_to
    return render_template('participant.html', name=name.title(), giving_to=giving_to)

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    polyanna = polynanna.main()
    app.run()

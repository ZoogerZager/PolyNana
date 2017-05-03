from flask import Flask
from flask import render_template
import polynanna


app = Flask(__name__)

@app.route('/')
def polyapp(participants=None):
    return render_template('index.html', polyanna=polyanna)

@app.route('/<name>')
def result(name=None):
    if name:
        giving_to = polyanna.get_participant_by_name(name).giving_to
        return render_template('participant.html', name=name, giving_to=giving_to)
    else:
        return render_template('test.html')

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    polyanna = polynanna.main()
    app.run()

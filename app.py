from flask import Flask, render_template, redirect, url_for
import polynanna


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', polyanna=polyanna)

@app.route('/<name>')
def result(name=None):
    try:
        giving_to = polyanna.get_participant_by_name(name).giving_to
        return render_template('result.html', name=name.title(), giving_to=giving_to)
    except:
        return redirect(url_for('index'))

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    polyanna = polynanna.main()
    app.run()

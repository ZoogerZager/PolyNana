from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from models import db, Person


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
db.init_app(app)
Bootstrap(app)

@app.route('/')
def index():
    participants = Person.query.all()
    return render_template('index.html', participants=participants)


@app.route('/<name>')
def result(name):
    try:
        person = Person.query.filter(Person.name==name.title()).first_or_404()
        return render_template('result.html', name=person.name, giving_to=person.giving_to)
    except:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

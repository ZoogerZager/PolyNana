from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from models import db, Person
import polynanna
import sys


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
    name = name.lower()
    try:
        person = Person.query.filter(Person.slug==name).first_or_404()
        return render_template('result.html', name=person.name, giving_to=person.giving_to)
    except:
        return redirect(url_for('index'))

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    if 'createdb' in sys.argv:
        with app.app_context():
            db.create_all()
        print('Database created!')
    elif 'seeddb' in sys.argv:
        with app.app_context():
            polyanna = polynanna.main()
            for p in polyanna.participants:
                entry = Person(slug=p.name.lower(), name=p.name, giving_to=p.giving_to)
                db.session.add(entry)
                db.session.commit()
    else:
        # polyanna = polynanna.main()
        app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), nullable=False)
    giving_to = db.Column(db.String(128), nullable=False)

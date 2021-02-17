from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    questions = db.relationship('Question')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000000000))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    user_name = db.Column(db.String, db.ForeignKey('user.user_name'))
    answers = db.relationship('Answer')

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000000000))
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_data = db.Column(db.Integer, db.ForeignKey('question.data'))
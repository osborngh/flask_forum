from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user

from . import db
from .models import Question, Answer

views = Blueprint('views', __name__)


@views.route('/user_home')
@login_required
def user_home():
    all_questions = Question.query.order_by(Question.date).all()
    return render_template('user_home.html', user=current_user, all_questions=all_questions)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)


@views.route('/user_home/questions', methods=['GET', 'POST'])
@login_required
def questions():
    if request.method == 'POST':
        question = request.form.get('question')

        if len(question) < 1:
            flash('Question is too short, Please try again', category='error')
        else:
            new_question = Question(data=question, user_name=current_user.user_name)
            db.session.add(new_question)
            db.session.commit()
            flash("Question Posted", category='success')
            return redirect('/user_home')
    return render_template('questions.html', user=current_user)


@views.route('/user_home/replys', methods=['GET', 'POST'])
@login_required
def answers():
    question = Answer.query.get(Answer.question_id)
    answers = Answer.query.order_by(Answer.question_id).all()
    if request.method == 'POST':
        reply = request.form.get('answer')

        if len(reply) < 1:
            flash("Reply is too short", category='error')
        else:
            new_reply = Answer(data=reply, user_name=current_user.user_name)
            db.session.add(new_reply)
            db.session.commit()
            flash("Answer Posted", category='success')
            return redirect('/user_home')
    return render_template('replys.html', user=current_user, question=question, answers=answers)

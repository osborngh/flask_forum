from flask import Blueprint, flash, redirect
from .models import User
from . import db


misc_func = Blueprint('misc_func', __name__)

@misc_func.route('/user_home/delete/<int:id>')
def delete_questions(id):
    if user.is_authenticated:
        question = User.query.get_or_404(id)
        db.session.delete(question)
        db.session.commit()
        return redirect('/user_home')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import random

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "437820302803-[]33231203\'\e[23042309-4230418209477386187628978712sdhgdkyusjdgwyuiryuiKJ,yirtrhjg7R5TYU7klU8y7uYUIY768Io"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .misc_func import misc_func

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    app.register_blueprint(misc_func, url_prefix = '/')

    from .models import Question, User
    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
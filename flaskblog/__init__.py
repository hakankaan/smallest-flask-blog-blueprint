import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

login_manager = LoginManager()
mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager.login_view = 'users.login' # To declare where is login page
login_manager.login_message_category = 'info'  # To declare message class.



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    return app
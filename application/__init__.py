from functools import wraps
from flask_login import LoginManager, current_user
from os import urandom
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

app.config["SECRET_KEY"] = urandom(32)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään."


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated():
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
from application import views
from application.kiireellisyysluokka import models
from application.kiireellisyysluokka import views

from application.tunti import models

from application.auth import models
from application.auth.models import User



from application.paiva import models
from application.paiva import views

from application.viikko import models
from application.viikko import views

from application.auth import views
try: 
    db.create_all()
except:
    pass
from application.tunti import views



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

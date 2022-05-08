from flask import Flask, render_template
from .extensions import db, bcrypt, login_manager
from anoopdev.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this is very secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    bcrypt.init_app(app)

    from anoopdev.auth import views
    app.register_blueprint(views.auth_view)

    from anoopdev.articles import views
    app.register_blueprint(views.articles_view)

    @app.route('/')
    def home():
        return render_template('home.html')
    return app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'briscola.sqlite'),
        SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(app.instance_path, 'briscolaWeb.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Init DB (https://hackersandslackers.com/flask-sqlalchemy-database-models/)
    db.init_app(app)

    socketio = SocketIO(app)

    with app.app_context():
        from . import routes

        # Create tables for our models
        db.create_all()

        # Register blueprints
        app.register_blueprint(routes.bp)
        
        return app




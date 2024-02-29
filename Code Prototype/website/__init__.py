from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this is the foosaForce APP'


    from .views import views    # each blueprint must be imprted into the init file
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')   # each blueprint must be registered, and the prefix for the url must be defined... this is the root, so we keep it as slash
    app.register_blueprint(auth, url_prefix='/')


    return app


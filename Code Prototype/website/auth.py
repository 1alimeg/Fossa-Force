from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"


@auth.route('/sign-up')
def signUp():
    return "<h1>Sign Up</h1>"





# this will be what you want to have at the top of every different view... each must be a seperate blueprint.
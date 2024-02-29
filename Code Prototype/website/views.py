from flask import Blueprint


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Hello</h1>"




# small little python trick that I learned... when you have a function, if you type "pass" down within it,
# it won't return an error
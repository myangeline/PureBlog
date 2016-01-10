from flask import Blueprint, render_template

__author__ = 'sunshine'

home = Blueprint('home', __name__, template_folder='templates',
                 static_url_path='/home/static', static_folder='static')


@home.route('/')
def index():
    return render_template('home/index.html')

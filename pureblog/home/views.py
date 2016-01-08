from flask import Blueprint, render_template

__author__ = 'sunshine'

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home.route('/')
def index():
    return render_template('layout.html')

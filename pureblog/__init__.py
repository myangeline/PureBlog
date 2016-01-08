from flask import Flask

from .home.views import home

__author__ = 'sunshine'

app = Flask(__name__)
app.config.from_object('pureblog.config')
app.config.from_pyfile('config.py')

# 蓝图注册
app.register_blueprint(home)

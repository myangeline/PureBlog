import datetime

from flask import Flask

from pureblog.admin.views import admin
from .home.views import home

__author__ = 'sunshine'

app = Flask(__name__)
app.config.from_object('pureblog.config')
app.config.from_pyfile('config.py')

app.permanent_session_lifetime = datetime.timedelta(days=1)

# 蓝图注册
app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')

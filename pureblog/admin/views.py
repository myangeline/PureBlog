from flask import Blueprint, render_template, request, jsonify
from flask.ext.wtf import Form

from pureblog.utils.mongodbutil import MongodbUtil

admin = Blueprint('admin', __name__, template_folder='templates',
                  static_url_path='/admin/static', static_folder='static')

mongodb = MongodbUtil()


@admin.route('/')
def index():
    return render_template('admin/layout.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = Form()
    if request.method == 'GET':
        return render_template('admin/login.html', form=form)
    else:
        user = mongodb.get_user('admin')
        print(user)
        print(request.values)
        return jsonify(request.values)

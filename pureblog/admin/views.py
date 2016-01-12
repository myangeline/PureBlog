from flask import Blueprint, render_template, request, jsonify, redirect, url_for

from pureblog.admin.wtfform import LoginForm, RegisterForm, ForgetForm
from pureblog.utils.convertutil import convert_str2int
from pureblog.utils.encryptutil import md5
from pureblog.utils.mongodbutil import MongodbUtil
from pureblog.utils.statusutil import error, ok

admin = Blueprint('admin', __name__, template_folder='templates',
                  static_url_path='/admin/static', static_folder='static')

mongodb = MongodbUtil()


@admin.route('/')
def index():
    return render_template('admin/layout.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    forget_form = ForgetForm(request.form)
    reg_form = RegisterForm(request.form)
    form_type = convert_str2int(request.values.get('form_type', 0))
    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongodb.get_user(form.username.data)
            if user:
                if user['pwd'] == md5(form.password.data):
                    return jsonify(ok('/admin/'))
                else:
                    return jsonify(error(30001))
            else:
                return jsonify(error(30002))
        else:
            return jsonify(error(30003))

    return render_template('admin/login.html', form=form, forget_form=forget_form,
                           reg_form=reg_form, form_type=form_type)


@admin.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        return redirect('admin')
    else:
        return jsonify(error(30004))

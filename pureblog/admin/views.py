import os

from flask import render_template, request, jsonify, session, redirect, url_for, Blueprint, current_app

from pureblog.admin.wtfform import LoginForm, RegisterForm, ForgetForm
from pureblog.instance.config import LOGIN_USERNAME, LOGIN_USER_HEADER_IMAGE
from pureblog.utils.convertutil import convert_str2int
from pureblog.utils.decoratorutil import login_required
from pureblog.utils.encryptutil import md5
from pureblog.utils.mongodbutil import mongodb
from pureblog.utils.statusutil import error, ok

admin = Blueprint('admin', __name__, template_folder='templates',
                  static_url_path='/admin/static', static_folder='static')


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


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
                if user['password'] == md5(form.password.data):
                    # session保存登录用户名和头像
                    session[LOGIN_USERNAME] = form.username.data
                    session[LOGIN_USER_HEADER_IMAGE] = user['header_img']
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
        user = mongodb.get_user(form.username.data)
        if user:
            return jsonify(error(30006))
        mongodb.add_user(form.fullname.data, form.email.data, form.address.data,
                         form.username.data, md5(form.password.data))
        return jsonify(ok('/admin/'))
    else:
        return jsonify(error(30004))


@admin.route('/logout', methods=['GET'])
@login_required
def logout():
    session.clear()
    return redirect(url_for('admin.login'))


# #####################博客管理###########################

@admin.route('/posts/write')
@login_required
def posts_write():
    """
    博客创作
    :return:
    """
    return render_template('admin/posts_write.html')


@admin.route('/posts/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files['posts_file']
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
    return 'hello'

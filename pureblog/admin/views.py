import os

from flask import render_template, request, jsonify, session, redirect, url_for, Blueprint, current_app

from pureblog.admin.wtfform import LoginForm, RegisterForm, ForgetForm, CategoryForm, PostsForm
from pureblog.instance.config import LOGIN_USERNAME, LOGIN_USER_HEADER_IMAGE, LOGIN_USER_ID
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
                    session[LOGIN_USER_ID] = str(user['_id'])
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

@admin.route('/posts/write', methods=['GET', 'POST'])
@login_required
def posts_write():
    """
    博客创作
    :return:
    """
    # todo 这里的文章保存验证有问题，现在先不管了
    user_id = session[LOGIN_USER_ID]
    form = PostsForm(request.form)
    if request.method == 'POST':

        return jsonify(ok('保存成功'))

    categories = mongodb.get_categories(user_id)
    return render_template('admin/posts_write.html', **locals())


@admin.route('/posts/list')
@login_required
def posts_list():
    pass


@admin.route('/posts/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files['posts_file']
    upload_folder = current_app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.mkdir(upload_folder)
    file.save(os.path.join(upload_folder, file.filename))
    return 'hello'


# #####################类别管理###########################

@admin.route('/category/add', methods=['GET', 'POST'])
@login_required
def category_add():
    form = CategoryForm(request.values)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_id = session[LOGIN_USER_ID]
            mongodb.add_category(user_id, form.data['category_name'])
            return jsonify(ok('保存成功'))
        else:
            return jsonify(error(40001))
    return render_template('admin/category_add.html', form=form)


@admin.route('/category/list', methods=['GET', 'POST'])
@login_required
def category_list():
    form = CategoryForm(request.values)
    user_id = session[LOGIN_USER_ID]
    if request.method == 'POST':
        if form.validate_on_submit():
            mongodb.add_category(user_id, form.data['category_name'])
            return jsonify(ok('保存成功'))
        else:
            return jsonify(error(40001))
    categories = mongodb.get_categories(user_id)
    return render_template('admin/category_list.html',
                           form=form, categories=categories)


@admin.route('/category/update', methods=['POST'])
@login_required
def category_update():
    category_id = request.values.get('category_id', None)
    category_name = request.values.get('category_name', None)
    if category_id and category_name:
        user_id = session[LOGIN_USER_ID]
        category = mongodb.get_categories(user_id, category_id)
        if not category:
            return jsonify(error(40003))
        if category and category_name != category['name']:
            mongodb.update_category(category_id, category_name)
            return jsonify(ok('修改成功'))
        else:
            return jsonify(error(40002))
    else:
        return jsonify(error(30007))


@admin.route('/category/delete', methods=['POST'])
@login_required
def category_delete():
    category_id = request.values.get('category_id', None)
    if category_id:
        mongodb.delete_category(category_id)
        return jsonify(ok('删除成功'))
    else:
        return jsonify(error(30007))

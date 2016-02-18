from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo

__author__ = 'sunshine'


class LoginForm(Form):
    username = StringField("用户名", validators=[DataRequired('用户名错误')])
    password = PasswordField("密码", validators=[DataRequired('密码错误')])


class RegisterForm(Form):
    fullname = StringField("姓名", validators=[DataRequired('姓名不可为空')])
    email = EmailField("Email", validators=[DataRequired('Email不可为空'), Email('Email格式错误')])
    address = StringField("地址", validators=[DataRequired('地址不可为空')])
    username = StringField("用户名", validators=[DataRequired('用户名不可为空')])
    password = PasswordField("密码", validators=[DataRequired('密码不可为空'), EqualTo('rpassword', '两次密码不一致')])
    rpassword = PasswordField("确认密码", validators=[DataRequired('确认密码不可为空')])
    tnc = BooleanField("", validators=[DataRequired('姓名不可为空')])


class ForgetForm(Form):
    email = EmailField('Email', validators=[DataRequired('Email不可为空'), Email('Email格式错误')])


class CategoryForm(Form):
    category_name = StringField("类别名称", validators=[DataRequired('类别名称不可为空')])


class PostsForm(Form):
    title = StringField("标题", validators=[DataRequired('标题不可为空')])
    summary = StringField("摘要", validators=[DataRequired('摘要不可为空')])
    posts_category = StringField("类别", validators=[DataRequired('类别不可为空')])
    posts_name = StringField("文件名", validators=[DataRequired('文件名不可为空')])
    is_public = IntegerField("是否发布", validators=[DataRequired('是否发布不可为空')])

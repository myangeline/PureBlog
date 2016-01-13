from functools import wraps

from flask import session, redirect, url_for

from pureblog.instance.config import LOGIN_USERNAME

__author__ = 'sunshine'


def login_required(func):
    """
    用户登录装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrap(**kwargs):
        # 判断是否登录
        if LOGIN_USERNAME not in session:
            return redirect(url_for('admin.login'))
        else:
            return func(**kwargs)
    return wrap

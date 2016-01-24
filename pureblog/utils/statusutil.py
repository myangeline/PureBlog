__author__ = 'sunshine'


code_map = {
    -1: '系统异常，请稍后重试',
    0: '成功',

    30001: '密码错误',
    30002: '用户名错误',
    30003: '用户名或密码错误',
    30004: '注册失败',
    30005: 'Email发送失败',
    30006: '用户名已存在',
    30007: '参数错误',

    40001: '类别名称错误',
    40002: '类别名称已存在',
    40003: '类别记录不存在',
}


def error(code):
    return {
        'code': code,
        'data': '',
        'error': code_map[code]
    }


def ok(data):
    return {
        'code': 0,
        'data': data,
        'error': ''
    }

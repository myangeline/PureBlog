import hashlib

__author__ = 'sunshine'


def md5(message, encoding='utf-8'):
    """
    md5加密
    :param message: 待加密字符
    :param encoding: 编码格式
    :return:
    """
    if isinstance(message, str):
        message = message.encode(encoding)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    return m.hexdigest()


# def md5_file()


if __name__ == '__main__':
    print(md5('abc'))
    pass

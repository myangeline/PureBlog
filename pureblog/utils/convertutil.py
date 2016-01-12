__author__ = 'sunshine'


def convert_str2int(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default


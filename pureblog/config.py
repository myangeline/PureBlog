import os

__author__ = 'sunshine'

DEBUG = True
BCRYPT_LEVEL = 13

CSRF_ENABLED = True
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/markdown')

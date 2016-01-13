import datetime

import pymongo

from pureblog.instance import config


class MongodbUtil(object):
    def __init__(self, host=config.HOST, port=config.PORT, user=config.USERNAME,
                 pwd=config.PASSWORD, db=config.DBNAME):
        client = pymongo.MongoClient(host, port, connect=False)
        db = client[db]
        db.authenticate(user, pwd, source=config.SOURCE)
        self.db = db

    def get_user(self, name):
        return self.db['dt_user'].find_one({'username': name})

    def add_user(self, fullname, email, address, username, password):
        doc = {
            'fullname': fullname,
            'email': email,
            'address': address,
            'username': username,
            'password': password,
            # 新注册的用户使用默认头像，以后可以修改
            'header_img': '/admin/admin/static/metronic/admin/layout/img/avatar3_small.jpg',
            'create_date': datetime.datetime.now()
        }
        self.db['dt_user'].insert(doc)

mongodb = MongodbUtil()


if __name__ == '__main__':
    mongodb = MongodbUtil()
    print(mongodb.get_user('admin'))
    pass

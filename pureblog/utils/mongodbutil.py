import datetime

import pymongo
from bson import ObjectId

from pureblog.instance import config


class MongodbUtil(object):
    def __init__(self, host=config.HOST, port=config.PORT, user=config.USERNAME,
                 pwd=config.PASSWORD, db=config.DBNAME):
        client = pymongo.MongoClient(host, port, connect=False)
        db = client[db]
        db.authenticate(user, pwd, source=config.SOURCE)
        self.db = db

    def get_user(self, name):
        """
        获取用户
        :param name:
        :return:
        """
        return self.db['dt_user'].find_one({'username': name})

    def add_user(self, fullname, email, address, username, password):
        """
        添加用户
        :param fullname:
        :param email:
        :param address:
        :param username:
        :param password:
        :return:
        """
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

    def add_category(self, user_id, name):
        """
        添加类别
        :param user_id:
        :param name:
        :return:
        """
        doc = {
            'user_id': user_id,
            'name': name,
            'create_date': datetime.datetime.now()
        }
        self.db['dt_categories'].insert(doc)

    def get_categories(self, user_id, category_id=None):
        """
        获取类别
        :param user_id:
        :param category_id:
        :return:
        """
        if category_id:
            return self.db['dt_categories'].find_one({'_id': ObjectId(category_id), 'user_id': user_id})
        else:
            return self.db['dt_categories'].find({'user_id': user_id})

    def delete_category(self, category_id):
        """
        删除类别
        :param category_id:
        :return:
        """
        self.db['dt_categories'].remove({'_id': ObjectId(category_id)})

    def update_category(self, category_id, name):
        """
        更新类别名称
        :param category_id:
        :param name:
        :return:
        """
        self.db['dt_categories'].update_one(
                {'_id': ObjectId(category_id)}, {'$set': {'name': name}})


mongodb = MongodbUtil()


if __name__ == '__main__':
    mongodb = MongodbUtil()
    print(mongodb.get_user('admin'))
    pass

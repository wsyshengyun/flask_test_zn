
from email.mime import base
import os 
# 生成secret_key密钥
# SECRET_KEY = os.urandom(24)
SECRET_KEY = '123456789'
CSRF_ENABLED = True  # 开启CSRF保护 
# 解决 The CSRF token is missing.
WTF_CSRF_CHECK_DEFAULT = True

basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = r"D:\\_python\\my"


class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        # 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = "sqlite:///D:/_python/my/flaskat/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    

from flask import current_app
current_app.logger.debug('config.py, SECRET_KEY : {}'.format(SECRET_KEY))
current_app.logger.debug('db post: {}'.format(Config.SQLALCHEMY_DATABASE_URI))
current_app.logger.debug('basedir : {}'.format(basedir))

import os 
# 生成secret_key密钥
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True  # 开启CSRF保护 
# 解决 The CSRF token is missing.
WTF_CSRF_CHECK_DEFAULT = True

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    

from flask import current_app
current_app.logger.debug('config.py, SECRET_KEY : {}'.format(SECRET_KEY))

import os 
# 生成secret_key密钥
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True  # 开启CSRF保护 
# 解决 The CSRF token is missing.
WTF_CSRF_CHECK_DEFAULT = True

from flask import current_app
current_app.logger.debug('config.py, SECRET_KEY : {}'.format(SECRET_KEY))
 
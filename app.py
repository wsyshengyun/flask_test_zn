from flask import Flask
# import config
from flask_bootstrap   import  Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


# 创建app
app = Flask(__name__)
bootstrap = Bootstrap(app)
# 日志功能 
with app.app_context():
    import log
    import config
    import routes
    import forms

# 解决flask shell抛出错误
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:/_python/my/flaskat/app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# app.config.from_object(config)
CSRFProtect(app)


db = SQLAlchemy(app)
migrate = Migrate(app, db )



import models
app.logger.debug('in app.py')


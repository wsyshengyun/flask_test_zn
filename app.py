from flask import Flask
# import config
from flask_bootstrap   import  Bootstrap
from flask_wtf.csrf import CSRFProtect


# 创建app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# 日志功能 
with app.app_context():
    import log
    import config
    import routes
    import forms

app.config.from_object(config)
CSRFProtect(app)




app.logger.debug('in app.py')


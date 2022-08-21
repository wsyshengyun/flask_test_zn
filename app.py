from flask import Flask 
from flask import render_template
from flask_bootstrap   import  Bootstrap
# 创建app
app = Flask(__name__)

# 日志功能 
with app.app_context():
    import log


bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('test_bootstrap.html', name='wsy')


@app.route('/user/<name>')
def user(name):
    listname = {'wsy', 'liuruifei', 'wanglihang'}
    return render_template('test_bootstrap.html', name=name)

app.logger.debug('nihao')
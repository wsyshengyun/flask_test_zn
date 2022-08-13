from flask import Flask 
from flask import template_rendered, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hello World!</h1>"
    comments = ['baidu', 'taobao', 'wangyi', 'meituan']
    return render_template('index.html', comments=comments)
    return


@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello, {}!</h1>".format(name)
    # return render_template("./templates/user.html", name=name)
    listname = {'wsy', 'liuruifei', 'wanglihang'}
    return render_template("user.html", name=name, listname=listname)


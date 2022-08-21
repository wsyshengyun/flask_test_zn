from app import app 
from flask import render_template , flash, redirect, url_for
from forms import LoginForm 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        flash("Login requested for user{}, remember_me={}".format(
            form.username.data, form.remember_me.data
        ))     
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

from flask import current_app
current_app.logger.debug('routes.py')
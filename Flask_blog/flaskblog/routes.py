from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationFrom, LoginFrom
from flaskblog.models import User, Post

posts = [
  {
    'author': 'Praise Victor',
    'title' : 'Blog post 1',
    'content' : 'First post content',
    'date_posted' : 'November 26, 2024'
  },
  {
    'author': 'Stacy Miriam',
    'title' : 'Blog post 2',
    'content' : 'Second post content',
    'date_posted' : 'November 27, 2024'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationFrom()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!,', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginFrom()
  if form.validate_on_submit():
    if form.email.data == 'stacynjoki@gmail.com' and form.password.data == 'njoki':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='login', form=form)
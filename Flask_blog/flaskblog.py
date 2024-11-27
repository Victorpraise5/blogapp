from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginFrom

app = Flask(__name__)

app.config['SECRET_KEY'] = '2ccf1b201268796b9827dac6f4c659b9'

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

@app.route("/login")
def login():
  form = LoginFrom()
  return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
  app.run(debug=True)
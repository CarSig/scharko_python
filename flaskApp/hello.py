from flask import Flask, render_template,flash, redirect, url_for, request
from flask_wtf import FlaskForm    
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from redditapi import reddit
import requests
import pandas as pd
from auth import id, secret, username, password



app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name  
    
# with app.app_context():
#     print("Before create_all()")
#     print(db)
#     db.create_all()
#     print("After create_all()")    
# print('Database created')    
# Create a form class
class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit')

class RedditForm(FlaskForm):
    subreddit = StringField('Subreddit', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Submit')    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
     return render_template('user.html', name=name)

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('User added successfully!')
        # user = User(name=form.name.data, email=form.email.data)
        # db.session.add(user)
        db.session.commit()
        flash('User added successfully!')
        our_users = User.query.order_by(User.date_added)
        return render_template('user.html', name=form.name.data, ourUsers=our_users)
    return render_template('add_user.html', form=form)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Name submitted successfully!')
    return render_template('name.html', form=form, name=name)



@app.route('/reddit/<subreddit>', methods=['GET', 'POST'])
def reddit(subreddit):
    print('fetchin reddit data...')
    auth = requests.auth.HTTPBasicAuth(id, secret)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }

    headers = {'User-Agent': 'MyAPI/' + '0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    token = res.json()['access_token']
    headers['Authorization'] = f"bearer {token}"

    me = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    hot = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot', headers=headers)
    

    subreddit =[]

    for topic in hot.json()['data']['children']:
        post = {
    'title': [topic['data']['title']],
    'url': [topic['data']['url']],
    'num_comments': [topic['data']['num_comments']],
    'created': [topic['data']['created']],
    'subreddit': [topic['data']['subreddit']]
}

        subreddit.append(post)
   
    return render_template('reddit.html', subreddit=subreddit)



@app.route('/reddit', methods=['GET', 'POST'])
def redditChooser():
    subreddit = None
    # category = 'hot'
    print(request.method  )
    form = RedditForm()
   
    if request.method == 'POST':
        subreddit = form.subreddit.data
        form.subreddit.data = ''
        print('Form submitted')
        return redirect(url_for('reddit',subreddit=subreddit)  )  
        
    if request.method == 'GET':
        return render_template('redditChooser.html', form=form, subreddit=subreddit)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500







if __name__ == '__main__':
    app.run(debug=True)


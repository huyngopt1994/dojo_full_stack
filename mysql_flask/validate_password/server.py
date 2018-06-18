import sys
import os
import re
import datetime
from flask import Flask, flash, render_template,request, redirect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
from mysqlconnection import MYSQLConnector
app = Flask(__name__)
app.secret_key ='huyngo'
mysql = MYSQLConnector(app,'twitter')

REGEX_MAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

my_db = mysql.db

class Email(my_db.Model):
    id = my_db.Column(my_db.Integer, primary_key=True)
    name = my_db.Column(my_db.String(255))
    created_date = my_db.Column(my_db.DateTime, default=datetime.datetime.utcnow)


my_db.create_all()

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/', methods=['POST'])
def validate_email():
    if not REGEX_MAIL.match(request.form['email']):
        flash('Please invalid email')
        return redirect('/')
    # query to check duplicate or not
    if (Email.query.filter_by(name=request.form['email']).first()):
        return render_template("index.html",emails = Email.query.all())
    email = Email(name=request.form['email'])

    my_db.session.add(email)
    my_db.session.commit()
    flash("Your input is valid")
    return render_template("index.html",emails = Email.query.all())


app.run(debug=True)
import sys
import os
from flask import Flask,render_template, request, redirect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
from mysqlconnection import MYSQLConnector
app =Flask(__name__)

mysql =  MYSQLConnector(app, 'twitter')
my_db = mysql.db

class Friend(my_db.Model):
    id = my_db.Column(my_db.Integer, primary_key= True)
    first_name = my_db.Column(my_db.String(255))
    last_name = my_db.Column(my_db.String(255))
    occupation = my_db.Column(my_db.String(255))
my_db.create_all()
@app.route('/')
def show_all():

    return render_template('index.html',friends= Friend.query.all())

@app.route('/add_friend',methods=['POST'])
def add_friend():
    friend = Friend(first_name= request.form['first_name'],
                    last_name= request.form['last_name'],
                    occupation = request.form['occupation'])
    my_db.session.add(friend)
    my_db.session.commit()
    return redirect('/')

app.run(debug=True)




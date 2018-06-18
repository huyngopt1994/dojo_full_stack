from flask import Flask , session, render_template,redirect,request,jsonify
import random
app = Flask(__name__)

app.secret_key = "HuySecret"

@app.route('/')
def index():
     if "guess_number" not in session:
         session['guess_number'] = random.randint(1,100)
     return render_template('index.html')

@app.route('/', methods=['POST'])
def check_number():
    print(request.form['number'])
    if int(request.form['number']) > session['guess_number']:
        message = "It's too low"
    elif int(request.form['number']) < session['guess_number']:
        message = "It's too high"

    return jsonify(message= message)

app.run(debug=True)
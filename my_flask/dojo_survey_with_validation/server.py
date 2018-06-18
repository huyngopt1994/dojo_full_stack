from flask import Flask, render_template,request, flash,redirect

app = Flask(__name__)
app.secret_key = 'xinchao'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if len(request.form['name']) == 0 or len(request.form['comment']) == 0:
		flash("Name or comment cannot be blank")
		return redirect('/')
	elif len(request.form['comment'] > 120):
		flash("The comment should not be larger 120")
	return render_template('result.html', name=request.form['name'],
						   location = request.form['location'],
						   language = request.form['language'],
						   comment = request.form['comment'])


app.run(debug=True)
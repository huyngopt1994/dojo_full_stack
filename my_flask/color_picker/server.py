from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',red=12,green=96,blue=222)

@app.route('/', methods=['POST'])
def updated_color():
	return render_template('index.html',red=request.form['red'],
		blue=request.form['blue'],
		green=request.form['green'])
	
app.run(debug=True)
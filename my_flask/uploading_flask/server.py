from flask import Flask, render_template,request, flash,redirect, url_for
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER ='/tmp/'
# limit extension because
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','py'])
app = Flask(__name__)
app.secret_key = 'xinchao'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename  and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
	if request.method == 'POST':
		# check if the post request has file part

		if 'file' not in request.files:
			flash('No file part')
			return redirect('/')
		file = request.files['file']
		# check filename is empty
		if file.filename == '':
			flash('No selected file')
			return redirect('/')

		if allowed_file(file.filename):
			# if filename is allowed file
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('index',filename=filename))
	else:
		#if file in allowed_file()
		return render_template('result.html',result=result )


app.run(debug=True)
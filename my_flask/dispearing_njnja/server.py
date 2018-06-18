from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/njnja')
def success():
	my_images= ['donatello.jpg','leonardo.jpg','michelangelo.jpg','raphael.jpg']
	return render_template('njnja.html',show_all=True,my_images=my_images)


@app.route('/njnja/<color>')
def project(color):
	images_dict ={
		'blue':'leonardo.jpg',
		'orange': 'michelangelo.jpg',
		'red': 'raphael.jpg',
		'purple':'donatello.jpg'
	}
	color = images_dict.get(color,'notapril.jpg')

	return render_template('njnja.html',show_all=False,color=color)

app.run(debug=True)
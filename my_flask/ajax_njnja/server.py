from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def render_character():

	my_images= {
	'purple':['nonatello.jpg',"You choose Nonatello"],
	'blue':['leonardo.jpg',"You choose leonardo"],
	'orange':['michelangelo.jpg',"You choose michelangelo"],
	'red':['raphael.jpg', "You choose raphael"]
	}
	result = my_images.get(request.form['color'],'No Image')

	return jsonify(image=result[0],message=result[1])

app.run(debug=True)
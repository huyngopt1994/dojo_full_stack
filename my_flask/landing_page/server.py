from flask import Flask,render_template,request, redirect
app =Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninja():
    return render_template("ninjas.html")
# this route will handle our form submission
# notice how we defined which HTTP method are allowed by this route
@app.route('/dojo/news')
def dojo():
    
    return render_template('dojos.html')

app.run(debug=True, port=8000)
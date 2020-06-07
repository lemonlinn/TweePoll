import TweePoll_API
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	return(render_template("index.html"))
	
@app.route('/inputs', methods = ['POST'])
def inputs():
	if request.method == "POST":
		if request.form['variable']:
			#return variable
			return(request.form['variable'])

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
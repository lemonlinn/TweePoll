import TweePoll_API
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	return(render_template("index.html"))
	
@app.route('/', methods = ['POST'])
def inputs():
	if request.method == "POST":
		if request.form['variable']:
			v = request.form['variable']
			return(v)

# BOOKMARK 6-7-2020: Trying to print streamer output underneath input field
@app.route('/output')
def outputs():
	streamer = TweePoll_API.MyStreamListener()
	s = streamer.main(t)
	return render_template("index.html", output = s)

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
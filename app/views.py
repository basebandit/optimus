from flask import render_template
from app import app

#maps to / in the url
@app.route('/')
#maps to /index in the url
@app.route('/index')
def index():
	project = "Optimus"
	name = "Devmars"
	return render_template('index.html',project=project,name=name)
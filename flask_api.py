from flask import Flask
#from farm import Ga 


app=Flask(__name__)

@app.route('/hello')
def hello_world():
	return "Hello World!"

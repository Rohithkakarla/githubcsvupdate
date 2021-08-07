from flask import Flask
from Model import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/print')
def modelrun():
    printcsv()
    return "success"

    
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)

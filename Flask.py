from flask import Flask
from Model import printcsv

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/print')
def modelrun():
    printcsv()
    return "Success Printing"
    
if __name__ == '__main__':
	app.run()
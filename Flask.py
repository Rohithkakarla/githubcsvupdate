from flask import Flask
from Model import *
import logging
import pandas as pd

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s : %(message)s')

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/print')
def modelrun():
    app.logger.info('Info level log')
    df = pd.read_csv("pima-indians-diabetesdata-pima-indians-diabetesdata.csv")
    app.logger.info(df.tail())
    return "success"

    
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)

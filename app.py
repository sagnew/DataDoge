from flask import Flask, render_template, request, redirect, json, jsonify
from dogeON import *
import urllib

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/test')
def test():
	return 'test'

if __name__ == '__main__':
	# if I am being run from the command line.
	app.run('0.0.0.0', debug = True)

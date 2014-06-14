from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['get', 'post', 'put', 'delete'])
def index():
    if request.method == 'GET':
        return "Naw"
    return "Hello"

if __name__ == '__main__':
    # if I am being run from the command line.
    app.run('0.0.0.0', port=7000, debug = True)

from flask import Flask, render_template, request, redirect, json, jsonify
import dogeON
import requests

app = Flask(__name__)

@app.route('/<path:url>', methods=['get', 'post', 'put', 'delete'])
def index(url):
    print url
    if request.method == 'GET':
        return requests.get(url, params=request.args).text
    return "Hello"

if __name__ == '__main__':
    # if I am being run from the command line.
    app.run('0.0.0.0', port=7000, debug = True)

from flask import Flask, render_template, request, redirect, json, jsonify
import dson
import requests

app = Flask(__name__)

@app.route('/<path:url>', methods=['get', 'post', 'put', 'delete'])
def index(url):
    print url
    if request.method == 'GET':
        return dson.dumps(requests.get(url, params=request.args).json())
    elif request.method == 'POST':
        res = requests.post(url, data=request.json)
        return dson.dumps(res.json())
    return "such 'error' much sorry wow"

if __name__ == '__main__':
    # if I am being run from the command line.
    app.run('0.0.0.0', port=7000, debug = True)

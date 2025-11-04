from flask import Flask, render_template, jsonify
import random


app = Flask(__name__)


@app.route('/data')
def data():
    result = {
        "value": random.randint(1,100)
    }
    return jsonify(result)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
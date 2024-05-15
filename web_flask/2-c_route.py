#!/usr/bin/python3
""" Here goes Every thing"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    """ """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cParam(text):
    """ """
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

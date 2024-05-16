#!/usr/bin/python3
""" Here goes Every thing"""
from flask import Flask, render_template

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
def c_param(text):
    """ """
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_param(text="is cool"):
    """ """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display(n):
    """ """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ """
    if n % 2 == 0:
        n = '{} is even'.format(n)
        return render_template('6-number_odd_or_even.html', n=n)
    else:
        n = '{} is odd'.format(n)
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

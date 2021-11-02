from flask import Flask, request, render_template, url_for

import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():  # put application's code here
    return render_template('portfolio-details.html')


@app.route('/table')
def table():  # put application's code here
    return render_template('table.html')

@app.route('/inner')
def inner():  # put application's code here
    return render_template('inner-page.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')


@app.route('/websites')
def websites():
    return render_template('websites.html')




if __name__ == '__main__':
    app.run(debug=True)

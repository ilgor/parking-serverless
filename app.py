# app.py

from flask import Flask, render_template

app = Flask(__name__, template_folder='static')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/bye')
def bye():
  return 'Good bye for now and come back again!'

@app.route('/hello')
def hello():
  return 'Hello World'


if __name__ == '__main__':
  app.run()
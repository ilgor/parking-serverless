# Flask Serverless Demo

## Prerequisites:
  - Python & Flask
  - Serverless Framework
  - AWS

## Steps to build and deploy:
  1. Create project folder: `mkdir parking-serverless && cd parking-serverless`
  2. Create package.json: `npm init -f`
  3. Install python related packges: `npm install --save-dev serverless-wsgi serverless-python-requirements`
  4. Create Virtual Environment: `python3 -m venv venv`
  5. Activate your venv: `source venv/bin/activate`
  6. Install Flask `pip install flask`
  7. Create file `app.py` and put the following code in it: 
  ```python
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
  ```
  7. Run locally on terminal `python app.py` and go to the URL
  8. create `serverless.yml`
  ```
  # serverless.yml
  service: serverless-flask

  plugins:
    - serverless-python-requirements
    - serverless-wsgi

  custom:
    wsgi:
      app: app.app
      packRequirements: false
    pythonRequirements:
      dockerizePip: non-linux

  provider:
    name: aws
    runtime: python3.6
    stage: dev
    region: us-east-1

  functions:
    app:
      handler: wsgi.handler
      events:
        - http: ANY /
        - http: 'ANY {proxy+}'
  ```
  9. create `python3 -m venv venv`
  10. `pip freeze > requirements.txt`
  11.  `sls deploy`

# Flask Serverless Demo
  1. Create project folder: `mkdir parking-serverless && cd parking-serverless`
  2. Create package.json: `npm init -f`
  3. Install python related packges: `npm install --save-dev serverless-wsgi serverless-python-requirements`
  4. Create file `app.py` and put the following code in it: 
  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def hello():
    return 'Hello World'

  @app.route('/bye')
  def bye():
    return 'Bye World'
  ```
  5. create `serverless.yml`
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
  6. create `python3 -m venv venv`
  7. `pip freeze > requirements.txt`
  8.  `sls deploy`

from flask import request, Flask
import json

app = Flask(__name__)
@app.route('/')

def hello_world():
  return 'server1'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.constant import METHOD

app = Flask(__name__)
CORS(app)

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
  try:
    # Input
    if request.form:
      data = request.form.to_dict()
      file = request.files['inputFile']
    else:
      data = request.get_json()

    # Output
    if data['method'] == METHOD['ECB']:
      data['result'] = 'ECB'
    elif data['method'] == METHOD['CBC']:
      data['result'] = 'CBC'
    elif data['method'] == METHOD['OFB']:
      data['result'] = 'OFB'
    elif data['method'] == METHOD['CFB']:
      data['result'] = 'CFB'
    elif data['method'] == METHOD['COUNTER']:
      data['result'] = 'Counter'

    return jsonify(data)
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
  try:
    # Input
    if request.form:
      data = request.form.to_dict()
      file = request.files['inputFile']
    else:
      data = request.get_json()

    # Output
    if data['method'] == METHOD['ECB']:
      data['result'] = 'ECB'
    elif data['method'] == METHOD['CBC']:
      data['result'] = 'CBC'
    elif data['method'] == METHOD['OFB']:
      data['result'] = 'OFB'
    elif data['method'] == METHOD['CFB']:
      data['result'] = 'CFB'
    elif data['method'] == METHOD['COUNTER']:
      data['result'] = 'Counter'
    
    return jsonify(data)
  except Exception as e:
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run()
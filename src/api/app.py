import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.constant import METHOD
from utils.ECB.service import extend_bit_ecb, encrypt_ecb, decrypt_ecb

app = Flask(__name__)
CORS(app)

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
  # Input
  if request.form:
    data = request.form.to_dict()
    file = request.files['inputFile']
  else:
    data = request.get_json()
    # Convert text to bit
    data['inputBit'] = ''.join(format(ord(char), '08b') for char in data['inputText'])
    print(data['inputBit'])

  # Output
  # Convert key to bit
  data['keyBit'] = ''.join(format(ord(char), '08b') for char in data['key'])
  # ECB
  if data['method'] == METHOD['ECB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_ecb(data['inputBit'], data['keyBit'])
    # Encrypt plainteks bit
    data['resultBit'] = encrypt_ecb(data['inputBit'], data['keyBit'])
    # Convert cipher bit to text
    data['result'] = ''
    for i in range(0, len(data['resultBit']), 8):
      data['result'] += chr(int(data['resultBit'][i:i+8], 2))
  elif data['method'] == METHOD['CBC']:
    data['result'] = 'CBC'
  elif data['method'] == METHOD['OFB']:
    data['result'] = 'OFB'
  elif data['method'] == METHOD['CFB']:
    data['result'] = 'CFB'
  elif data['method'] == METHOD['COUNTER']:
    data['result'] = 'Counter'

  return jsonify(data)

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
  # Input
  if request.form:
    data = request.form.to_dict()
    file = request.files['inputFile']
  else:
    data = request.get_json()
    # Convert text to bit
    data['inputBit'] = ''.join(format(ord(char), '08b') for char in data['inputText'])

  # Output
  # Convert key to bit
  data['keyBit'] = ''.join(format(ord(char), '08b') for char in data['key'])
  # ECB
  if data['method'] == METHOD['ECB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_ecb(data['inputBit'], data['keyBit'])
    # Decrypt plainteks bit
    data['resultBit'] = decrypt_ecb(data['inputBit'], data['keyBit'])
    # Convert cipher bit to text
    data['result'] = ''
    for i in range(0, len(data['resultBit']), 8):
      data['result'] += chr(int(data['resultBit'][i:i+8], 2))
  elif data['method'] == METHOD['CBC']:
    data['result'] = 'CBC'
  elif data['method'] == METHOD['OFB']:
    data['result'] = 'OFB'
  elif data['method'] == METHOD['CFB']:
    data['result'] = 'CFB'
  elif data['method'] == METHOD['COUNTER']:
    data['result'] = 'Counter'

  return jsonify(data)

if __name__ == '__main__':
  app.run()
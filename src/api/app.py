import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.constant import METHOD
from utils.ECB.service import extend_bit_ecb, encrypt_ecb, decrypt_ecb
from utils.CBC.service import extend_bit_cbc, encrypt_cbc, decrypt_cbc
from utils.CFB.service import extend_bit_cfb, encrypt_cfb, decrypt_cfb
from utils.OFB.service import extend_bit_ofb, encrypt_ofb, decrypt_ofb

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

  # Output
  # Convert key to bit
  data['keyBit'] = ''.join(format(ord(char), '08b') for char in data['key'])
  # ECB
  if data['method'] == METHOD['ECB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_ecb(data['inputBit'], data['keyBit'])
    # Encrypt plainteks bit
    data['resultBit'] = encrypt_ecb(data['inputBit'], data['keyBit'])
  # CBC
  elif data['method'] == METHOD['CBC']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_cbc(data['inputBit'], data['keyBit'])
    # Encrypt plainteks bit
    data['resultBit'] = encrypt_cbc(data['inputBit'], data['keyBit'])
  elif data['method'] == METHOD['OFB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_cfb(data['inputBit'], data['encryptionLength'])
    # Encrypt plainteks bit
    data['resultBit'] = encrypt_ofb(data['inputBit'], data['keyBit'], data['encryptionLength'])
  elif data['method'] == METHOD['CFB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_cfb(data['inputBit'], data['encryptionLength'])
    # Encrypt plainteks bit
    data['resultBit'] = encrypt_cfb(data['inputBit'], data['keyBit'], data['encryptionLength'])
  elif data['method'] == METHOD['COUNTER']:
    data['result'] = 'Counter'

  # Convert cipher bit to text
  data['result'] = ''
  for i in range(0, len(data['resultBit']), 8):
    data['result'] += chr(int(data['resultBit'][i:i+8], 2))

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
  # CBC
  elif data['method'] == METHOD['CBC']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_cbc(data['inputBit'], data['keyBit'])
    # Decrypt plainteks bit
    data['resultBit'] = decrypt_cbc(data['inputBit'], data['keyBit'])
  elif data['method'] == METHOD['OFB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_ofb(data['inputBit'], data['encryptionLength'])
    # Encrypt plainteks bit
    data['resultBit'] = decrypt_cfb(data['inputBit'], data['keyBit'], data['encryptionLength'])
  elif data['method'] == METHOD['CFB']:
    # Extend plainteks bit
    data['inputBit'] = extend_bit_cfb(data['inputBit'], data['encryptionLength'])
    # Decrypt plainteks bit
    data['resultBit'] = decrypt_cfb(data['inputBit'], data['keyBit'], data['encryptionLength'])
  elif data['method'] == METHOD['COUNTER']:
    data['result'] = 'Counter'

  # Convert cipher bit to text
  data['result'] = ''
  for i in range(0, len(data['resultBit']), 8):
    data['result'] += chr(int(data['resultBit'][i:i+8], 2))

  return jsonify(data)

if __name__ == '__main__':
  app.run()
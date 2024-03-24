import base64

# Input
def get_request_mode(request,mode_operation):
    file_name = ""
    if request.form:
        data = request.form.to_dict()
        file = request.files['inputFile']
        file_name = file.filename
        data['inputBit'] = ''.join(format(byte, '08b') for byte in file.read())
        data['encryptionLength'] = int(data['encryptionLength'])
    else:
        data = request.get_json()
        # Convert text to bit
        if(mode_operation==1):
            encoded_bytes = base64.b64decode(data['inputText'])
            encoded_string = encoded_bytes.decode('utf-8')
            data['inputText'] = encoded_string
        data['inputBit'] = ''.join(format(ord(char), '08b') for char in data['inputText'])
    
    # Convert key to bit
    data['keyBit'] = ''.join(format(ord(char), '08b') for char in data['key'])

    return data, file_name

# Output
def bit_to_file(file_name, text, mode_operation):
    if mode_operation == 0:
        root_dir = 'output/[ENCRYPTED]'
        mode = 'encrypted'
    else:
        root_dir = 'output/[DECRYPTED]'
        mode = 'decrypted'

    result = bytes([int(text[i:i+8], 2) for i in range(0, len(text), 8)])
    with open(f'{root_dir} {file_name}', 'wb') as file:
        file.write(result)

    result = f'File has been {mode} in {root_dir} {file_name}'

    return result

def bit_to_text(text, mode_operation):
    result = ''

    for i in range(0, len(text), 8):
        result += chr(int(text[i:i+8], 2))

    # Original string

    # Encode the string into base64
    if(mode_operation==0):
        encoded_bytes = base64.b64encode(result.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        result = encoded_string

    return result

def get_output_result(form, text, mode_operation, file_name):
    if form:
        res = bit_to_file(file_name, text, mode_operation)
    else:
        res = bit_to_text(text, mode_operation)
    return res
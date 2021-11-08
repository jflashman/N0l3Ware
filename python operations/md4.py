# pip install hashlib

import hashlib

def md4(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.md4(encoded_input).hexdigest()
    return hashed_input
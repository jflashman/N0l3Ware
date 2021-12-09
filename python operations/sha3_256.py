# pip install hashlib

import hashlib

def sha3_256(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha3_256(encoded_input).hexdigest()
    return hashed_input


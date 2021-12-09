# pip install hashlib

import hashlib

def sha224(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha224(encoded_input).hexdigest()
    return hashed_input

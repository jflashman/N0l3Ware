# pip install hashlib

import hashlib

def sha384(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha384(encoded_input).hexdigest()
    return hashed_input

# pip install hashlib

import hashlib

def blake2b(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.blake2b(encoded_input).hexdigest()
    return hashed_input
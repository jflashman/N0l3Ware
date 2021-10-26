import hashlib

def sha3_334(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha3_334(encoded_input).hexdigest()
    return hashed_input

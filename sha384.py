import hashlib

def sha284(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha284(encoded_input).hexdigest()
    return hashed_input

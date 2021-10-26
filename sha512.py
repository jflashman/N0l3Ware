import hashlib

def sha512(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha512(encoded_input).hexdigest()
    return hashed_input

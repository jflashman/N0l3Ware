import hashlib

def sha1(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.sha1(encoded_input).hexdigest()
    return hashed_input

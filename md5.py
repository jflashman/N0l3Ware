import hashlib

def md5(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.md5(encoded_input).hexdigest()
    return hashed_input

import hashlib

def blake2s(input):
    encoded_input = input.encode('utf-8')
    hashed_input = hashlib.blake2s(encoded_input).hexdigest()
    return hashed_input

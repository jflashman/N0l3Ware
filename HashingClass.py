import hashlib
from Crypto.Hash import MD2

class HashingClass:
    def blake2b(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.blake2b(encoded_input).hexdigest()
        return hashed_input

    def blake2s(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.blake2s(encoded_input).hexdigest()
        return hashed_input

    def md2(input):
        val = MD2.new()
        encoded_input = input.encode('utf-8')
        val.update(encoded_input)
        hashed_input = val
        hashed_input = hashed_input.hexdigest()
        return hashed_input

    def md4(input):
        input = hashlib.new('md4', input.encode('utf-8'))
        hashed_input = input.hexdigest()
        return hashed_input

    def md5(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.md5(encoded_input).hexdigest()
        return hashed_input

    def sha1(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha1(encoded_input).hexdigest()
        return hashed_input

    def sha224(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha224(encoded_input).hexdigest()
        return hashed_input

    def sha256(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha256(encoded_input).hexdigest()
        return hashed_input

    def sha384(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha384(encoded_input).hexdigest()
        return hashed_input

    def sha3_224(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha3_224(encoded_input).hexdigest()
        return hashed_input

    def sha3_256(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha3_256(encoded_input).hexdigest()
        return hashed_input

    def sha3_384(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha3_384(encoded_input).hexdigest()
        return hashed_input

    def sha3_512(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha3_512(encoded_input).hexdigest()
        return hashed_input

    def sha512(input):
        encoded_input = input.encode('utf-8')
        hashed_input = hashlib.sha512(encoded_input).hexdigest()
        return hashed_input

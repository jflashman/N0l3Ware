import hashlib
from Crypto.Hash import MD2

class HashingClass:
    def __init__(self,input):
        self.input = input

    def blake2b(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.blake2b(encoded_input).hexdigest()
        return hashed_input

    def blake2s(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.blake2s(encoded_input).hexdigest()
        return hashed_input

    def md2(self):
        val = MD2.new()
        encoded_input = self.input.encode('utf-8')
        val.update(encoded_input)
        hashed_input = val
        hashed_input = hashed_input.hexdigest()
        return hashed_input

    def md4(self):
        self.input = hashlib.new('md4', self.input.encode('utf-8'))
        hashed_input = self.input.hexdigest()
        return hashed_input

    def md5(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.md5(encoded_input).hexdigest()
        return hashed_input

    def sha1(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha1(encoded_input).hexdigest()
        return hashed_input

    def sha224(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha224(encoded_input).hexdigest()
        return hashed_input

    def sha256(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha256(encoded_input).hexdigest()
        return hashed_input

    def sha384(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha384(encoded_input).hexdigest()
        return hashed_input

    def sha3_224(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha3_224(encoded_input).hexdigest()
        return hashed_input

    def sha3_256(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha3_256(encoded_input).hexdigest()
        return hashed_input

    def sha3_384(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha3_384(encoded_input).hexdigest()
        return hashed_input

    def sha3_512(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha3_512(encoded_input).hexdigest()
        return hashed_input

    def sha512(self):
        encoded_input = self.input.encode('utf-8')
        hashed_input = hashlib.sha512(encoded_input).hexdigest()
        return hashed_input

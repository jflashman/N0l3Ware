#Missing: Decryptions for OFB, CTR modes. Encryptions/Decryptions for ECB Modes

import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import scrypt
from base64 import b64encode, b64decode
from secrets import token_bytes



class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encryptCBC(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def encryptCFB(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def encryptOFB(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def encryptCTR(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_CTR)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")

    def encryptGCM(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_GCM)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")

    def encryptECB(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")




    def decryptCBC(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def decryptCFB(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def decryptOFB(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def decryptCTR(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(self.key, AES.MODE_CTR)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def decryptGCM(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def decryptECB(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(self.key, AES.MODE_ECB)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]


msg = input('Enter a message: ')
key = input('Enter a key: ')

p = AESCipher(key).encryptCBC(msg)
print('Encrypted value CBC: ', AESCipher(key).encryptCBC(msg))
print('Encrypted value CFB: ', AESCipher(key).encryptCFB(msg))
print('Encrypted value OFB: ', AESCipher(key).encryptOFB(msg))
print('Encrypted value CTR: ', AESCipher(key).encryptCTR(msg))
print('Encrypted value GCM: ', AESCipher(key).encryptGCM(msg))
print('Encrypted value ECB: ', AESCipher(key).encryptECB(msg))


print('Decrypted value CBC: ', AESCipher(key).decryptCBC(p))
print('Decrypted value CFB: ', AESCipher(key).decryptCFB(p))
print('Decrypted value OFB: ', AESCipher(key).decryptOFB(p))
print('Decrypted value CTR: ', AESCipher(key).decryptCTR(p))
print('Decrypted value GCM: ', AESCipher(key).decryptGCM(p))
print('Decrypted value ECB: ', AESCipher(key).decryptECB(p))



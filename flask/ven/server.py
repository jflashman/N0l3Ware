from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Crypto.Hash import MD2
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import scrypt
from base64 import b64encode, b64decode
from secrets import token_bytes
import hashlib



key = token_bytes(16)

app = Flask(__name__)
CORS(app, support_credentials=True)

def eEAX(msg):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_EAX, iv)
    nonce = cipher.nonce
    ciphertext , tag = cipher.encrypt_and_digest(msg.encode('ascii'))

    return nonce, ciphertext, tag

def dEAX(nonce, ciphertext):

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')
    
    
class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def eCBC(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def eCFB(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def eOFB(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def eCTR(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_CTR)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")

    def eGCM(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_GCM)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")

    def eECB(self, plain_text):
        plain_text = self.__pad(plain_text)
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")



    def dCBC(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def dCFB(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def dOFB(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def dCTR(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(self.key, AES.MODE_CTR)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def dGCM(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def gECB(self, encrypted_text):
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

    


@app.route("/members", methods=["GET"])
def members():
    response = {"Members": ["hello", "helo1", "Hello2"]}
    return response


@app.route("/md2", methods=["GET"])
@cross_origin(supports_credentials=True)
def md2():
    h = MD2.new()
    val = request.args.get('input')
    h.update(val.encode('ascii'))
    result = h.hexdigest()
    return jsonify(result)


@app.route("/md4", methods=["GET"])
@cross_origin(supports_credentials=True)
def md4():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.new('md4', encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/md5", methods=["GET"])
@cross_origin(supports_credentials=True)
def md5():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.new('md5', encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha1", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha1():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha1(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha224", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha224():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha224(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha256", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha256():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha256(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha384", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha384():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha384(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha512", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha512():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha512(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha3224", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha3224():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha3_224(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha3256", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha3256():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha3_256(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha3384", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha3384():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha3_384(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/sha3512", methods=["GET"])
@cross_origin(supports_credentials=True)
def sha3512():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.sha3_512(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/blake2s", methods=["GET"])
@cross_origin(supports_credentials=True)
def blake2s():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.blake2s(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/blake2b", methods=["GET"])
@cross_origin(supports_credentials=True)
def blake2b():
    val = request.args.get('input')
    encoded_input = val.encode('utf-8')
    hashed_input = hashlib.blake2b(encoded_input).hexdigest()
    return jsonify(hashed_input)


@app.route("/bin2dec", methods=["GET"])
@cross_origin(supports_credentials=True)
def bin2dec():
    error_msg = "Error in Input!\n"
    result = 0 # placeholder for final conversion
    val = request.args.get('input')

    orig_binary = str(val) # convert to string to access each int

    for bin in orig_binary:     # checks if binary is valid
        if bin == "0" or bin == "1":
            pass
            # continue
        else:
            return(error_msg)
            exit(0)

    rev_binary = reversed(str(val))     # reverse binary to start converting

    for i, num in enumerate(rev_binary):    # converts for each binary
        power = 2**i
        if int(num) == 1:
            result += power
        else:
            result += 0

    return jsonify(result)


@app.route("/dec2bin", methods=["GET"])
@cross_origin(supports_credentials=True)
def dec2bin():
    val = request.args.get('input')
    error_msg = "Error -- invalid input. Input decimal number"

    if str(val).isdigit():  # checks if devimal is valid
        # conversion from decimal to binary
        num = int(val)
        final_binary = ""
        while (num > 0):
            temp = int(float(num % 2))
            final_binary = str(temp) + final_binary
            num = (num - temp) / 2

        # end of conversion
        return jsonify(final_binary)

    else:
        return jsonify(error_msg)
      # print("Error in Input!\n")

@app.route("/xor", methods=["GET"])
@cross_origin(supports_credentials=True)
def xor():
    val = str(request.args.get('input'))
    if (len(val.partition("xor")) > 3):
        return jsonify("Too many operators!")

    val1 = int(val.partition("xor")[0])
    val2 = int(val.partition("xor")[2])
        
    return jsonify(val1 ^ val2)



@app.route("/or", methods=["GET"])
@cross_origin(supports_credentials=True)
def orr():
    val = str(request.args.get('input'))
    if (len(val.partition("or")) > 3):
        return jsonify("Too many operators!")

    val1 = int(val.partition("or")[0])
    val2 = int(val.partition("or")[2])

    print(val1 | val2)
        
    return jsonify(val1 | val2)

@app.route("/and", methods=["GET"])
@cross_origin(supports_credentials=True)
def andd():
    val = str(request.args.get('input'))
    if (len(val.partition("and")) > 3):
        return jsonify("Too many operators!")

    val1 = int(val.partition("and")[0])
    val2 = int(val.partition("and")[2])
        
    return jsonify(val1 & val2)

@app.route("/not", methods=["GET"])
@cross_origin(supports_credentials=True)
def nott():
    
    val = str(request.args.get('input'))
    if (len(val.partition("not")) > 3):
        return jsonify("Too many operators!")

    val1 = int(val.partition("not")[0])
    val2 = int(val.partition("not")[2])
        
    return jsonify(~val1)



@app.route("/encryptCBC", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptCBC():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg = val.partition(".")[2]


    return jsonify(AESCipher(key).eCBC(msg))

@app.route("/encryptCFB", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptCFB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg = val.partition(".")[2]

    return(jsonify(AESCipher(key).eCFB(msg)))

@app.route("/encryptOFB", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptOFB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg= val.partition(".")[2]

    return(jsonify(AESCipher(key).eOFB(msg)))

@app.route("/encryptCTR", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptCTR():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg= val.partition(".")[2]

    return(jsonify(AESCipher(key).eCTR(msg)))

@app.route("/encryptGCM", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptGCM():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg= val.partition(".")[2]

    return(jsonify(AESCipher(key).eGCM(msg)))

@app.route("/encryptECB", methods=['GET'])
@cross_origin(supports_credentials=True)
def encryptECB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    msg= val.partition(".")[2]

    return(jsonify(AESCipher(key).eECB(msg)))

@app.route("/decryptCBC", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptCBC():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]

    return(jsonify(AESCipher(key).dCBC(p)))

@app.route("/decryptCFB", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptCFB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]

   

    return(jsonify(AESCipher(key).dCFB(p)))

@app.route("/decryptOFB", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptOFB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]

    return(jsonify(AESCipher(key).dOFB(p)))

@app.route("/decryptCTR", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptCTR():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]

    return(jsonify(AESCipher(key).dCTR(p)))

@app.route("/decryptGCM", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptGCM():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]


    return(jsonify(AESCipher(key).dGCM(p)))

@app.route("/decryptECB", methods=['GET'])
@cross_origin(supports_credentials=True)
def decryptECB():
    val = str(request.args.get('input'))

    key = val.partition(".")[0]
    p = val.partition(".")[2]
    

    return(jsonify(AESCipher(key).dECB(p)))

if __name__ == "__main__":
    app.run(debug=True)

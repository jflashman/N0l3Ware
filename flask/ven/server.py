from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Crypto.Hash import MD2
import hashlib

app = Flask(__name__)

CORS(app, support_credentials=True)


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


if __name__ == "__main__":
    app.run(debug=True)

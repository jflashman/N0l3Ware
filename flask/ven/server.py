from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
from Crypto.Hash import MD2

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
    return result


if __name__ == "__main__":
    app.run(debug=True)

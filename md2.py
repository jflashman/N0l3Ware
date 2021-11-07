from Crypto.Hash import MD2

def md2(input):
    val = MD2.new()
    encoded_input = input.encode('utf-8')
    val.update(encoded_input)
    hashed_input = val
    hashed_input = hashed_input.hexdigest()
    return hashed_input
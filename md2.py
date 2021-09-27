# pip install pycryptodome

from Crypto.Hash import MD2

h = MD2.new()
val = input("Enter a value to convert to MD2: ")
h.update(val.encode('ascii'))
print(h.hexdigest())
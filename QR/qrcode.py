# pip install pyqrcode

import pyqrcode

def qrcode(input):
    url = pyqrcode.create(input)
    return url.eps('file.eps', scale=2)

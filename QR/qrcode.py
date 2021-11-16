import pyqrcode

url = pyqrcode.create('https://www.cs.fsu.edu/')
url.svg('fsu-url.svg', scale=8)
url.eps('fsu-url.eps', scale=2)
print(url.terminal(quiet_zone=1))

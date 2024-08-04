import ssl
from urllib.request import urlopen

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

x = urlopen("https://www.runoob.com/",context=context)

lines  = x.readlines()
for line in lines:
    print(line)
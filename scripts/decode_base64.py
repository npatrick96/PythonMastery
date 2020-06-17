#! /usr/local/bin/python3

import base64

f = open('./b64_file.txt', 'rb')
decoded_str = base64.b64decode(f.read())
print(decoded_str)
f.close()

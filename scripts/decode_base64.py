#! /usr/local/bin/python3

import base64

f = open('../sample_files/glossary_b64.txt', 'rb')
decoded_str = base64.b64decode(f.read()).decode('utf-8')
print(decoded_str)
f.close()

#! /usr/local/bin/python3

import base64
import zlib

f = open('../sample_files/glossary_b64_gzip.txt', 'rb')
decoded_str = zlib.decompress(base64.b64decode(f.read()), 16 + zlib.MAX_WBITS).decode('utf-8')
print(decoded_str)
f.close()

# source: https://stackoverflow.com/a/46522128

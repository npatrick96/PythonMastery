#! /usr/local/bin/python3

import gzip

exampleString = 'Gallia est omnis divisa in partes tres.'
print('example string: ' + exampleString)

compressed_value = gzip.compress(bytes(exampleString, 'utf-8'))
#print(type(compressed_value))
print('compressed bytes value of exampleString: ' + str(compressed_value))

exampleStringAgain = gzip.decompress(compressed_value).decode("utf-8")
#print(type(exampleStringAgain))
print('example string again after encoding and decoding: ' + str(exampleStringAgain))

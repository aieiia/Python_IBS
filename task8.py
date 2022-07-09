import os, sys

with open('input.txt', 'r') as inp: b = inp.read()
with open('output.txt', 'w') as outp: outp.write(b[::-1])
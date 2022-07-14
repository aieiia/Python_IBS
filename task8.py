import os, sys

inputfile = "C:/Users/AIlina/Desktop/input.txt"

with open(inputfile, 'r') as inp: b = inp.read()

with open(inputfile, 'r') as inp:
    for line in inp: print(line.rstrip(), end = '\n')

outputfile = "C:/Users/AIlina/Desktop/output.txt"

with open(outputfile, 'w+') as outp: outp.write(b[::-1])

with open(outputfile, 'r') as outp:
    for line in outp: print(line.rstrip(), end = '\n')
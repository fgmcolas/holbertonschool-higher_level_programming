#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argnumb =  len(sys.argv) - 1
if (argnumb == 0):
    print("0 arguments.")
elif (argnumb == 1):
    print("1 argument:")
else:
    print("{} arguments:".format(argnumb))

for arg in range(1, len(sys.argv)):
    print("{}: {}".format(arg, sys.argv[arg]))

#!/usr/bin/python3
def uppercase(text):
    for char in text:
        if 97 <= ord(char) <= 122:
            upper = chr(ord(char) - 32)
            print("{upper}".format(char), end="")
        else:
            print("{}".format(char), end="")
    print("")

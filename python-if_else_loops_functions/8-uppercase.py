#!/usr/bin/python3
def uppercase(text):
    for char in text:
        if 97 <= ord(char) <= 122:
            upper = chr(ord(char) - 32)
            print(f"{upper}", end="")
        else:
            print(f"{char}", end="")
    print("")

#!/usr/bin/python3
def uppercase(str):
    cap_str = ""

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            cap_char = ord(c) - 32
            cap_str += chr(cap_char)
        else:
            cap_str += c

    print("{}".format(cap_str))

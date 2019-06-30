#!/usr/bin/env python
# coding: utf-8
import string

def encoder(crypt_str, shift):
    crypt_list = list(crypt_str)
    plain_str = ""
    num = int(shift)
    for ch in crypt_list:
        ch = ord(ch)
        if ord('a') <= ch and ch <= ord('z'):
            ch = ch + num
            if ch > ord('z'):
                ch -= 26
        if ord('A') <= ch and ch <= ord('Z'):
            ch = ch + num
            if ch > ord('Z'):
                ch -= 26
        a = chr(ch)
        plain_str += a

    print (plain_str)

crypt_str = input("Crypto text: ")
#shift = raw_input("Shift?: ")
print("!----- decode -----!")
for shift in range(26):
    encoder(crypt_str, shift)

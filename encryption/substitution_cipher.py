# encryption/substitution_cipher.py

import string

def substitution_cipher(text, key):
    alphabet = string.ascii_uppercase
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key[alphabet.index(char)]
            else:
                result += key[alphabet.index(char.lower())].lower()
        else:
            result += char
    return result

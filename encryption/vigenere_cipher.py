# encryption/vigenere_cipher.py

import string

def vigenere_cipher(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + ord(key[key_index]) - 2 * 65) % 26 + 65)
            else:
                result += chr((ord(char) + ord(key[key_index]) - 2 * 97) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

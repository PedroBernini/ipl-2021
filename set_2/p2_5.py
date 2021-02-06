# Programa para realizar a Cifra de César.
import string

NUMBERS = list(map(lambda x: str(x), range(10)))
ALPHABET = list(string.ascii_lowercase)
CIPHER_ALPHABET = dict(zip(ALPHABET, list(range(len(ALPHABET)))))

def transformCharNumber(charNumber, n):
    return str((int(charNumber) + n) % 10)

def transformKey(key, n):
    return (key + n) % 26

def caesar_cipher(text, n):
    finalText = ''
    for char in text:
        char = char.lower()
        if char in ALPHABET:
            key = CIPHER_ALPHABET[char]
            key = transformKey(key, n)
            for letter, number in CIPHER_ALPHABET.items():
                if number == key:
                    finalText += letter
        elif char in NUMBERS:
            number = transformCharNumber(char, n)
            finalText += number
        else:
            finalText += char
    return finalText
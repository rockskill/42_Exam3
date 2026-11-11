#!/usr/bin/env python3


def whisper_cipher(text: str, shift: int) -> str:
    if len(text) == 0:
        return text
    text_ciphered: str = ""
    for c in text:
        if c.islower():
            text_ciphered += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c.isupper():
            text_ciphered += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            text_ciphered += c
    return text_ciphered


if __name__ == "__main__":
    # Test case 1: "khoor"
    print(whisper_cipher("hello", 3))
    # Test case 2: "Ifmmp Xpsme!"
    print(whisper_cipher("Hello World!", 1))
    # Test case 3: "abc"
    print(whisper_cipher("xyz", 3))
    # Test case 4: "FGH123ijk"
    print(whisper_cipher("ABC123def", 3))
    # Test case 5: ""
    print(whisper_cipher("", 10))
    # Test case 6: "xyz"
    print(whisper_cipher("abc", -3))

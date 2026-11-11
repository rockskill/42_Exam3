#!/usr/bin/env python3


"""
ASSIGNMENT:
Write a function that checks if a string is a palindrome,
ignoring spaces and case, only consider alphabetic characters
for the comparison.
"""


def echo_validator(text: str) -> bool:
    if len(text) <= 0:
        return False
    text_without_spaces: str = ""
    for c in text:
        if c != ' ':
            text_without_spaces += c
    if len(text_without_spaces) == 0:
        return False
    for i in range(len(text_without_spaces) // 2):
        if text_without_spaces[i].lower() != text_without_spaces[-i-1].lower():
            return False
    return True


if __name__ == "__main__":
    # Test case 1: True
    print(echo_validator("racecar"))
    # Test case 2: True
    print(echo_validator("A man a plan a canal Panama"))
    # Test case 3: False
    print(echo_validator("race a car"))
    # Test case 4: True
    print(echo_validator("Was it a car or a cat I saw"))
    # Test case 5: False
    print(echo_validator("hello"))
    # Test case 6: True
    print(echo_validator("Madam Im Adam"))
    # Test case 7: True
    print(echo_validator("madam"))
    # Test case 8: True
    print(echo_validator("Able was I ere I saw Elba"))
    # Test case 9: False
    print(echo_validator(""))

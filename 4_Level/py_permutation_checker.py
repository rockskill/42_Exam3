#!/usr/bin/env python3


"""
ASSIGNMENT:
Write a function that determines if two strings are permutations of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.
"""


def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c not in s2:
            return False
    for c in s2:
        if c not in s1:
            return False
    return True


if __name__ == "__main__":
    # Test case 1: True
    print(string_permutation_checker("abc", "bca"))
    # Test case 2: False
    print(string_permutation_checker("abc", "def"))
    # Test case 3: True
    print(string_permutation_checker("listen", "silent"))
    # Test case 4: False
    print(string_permutation_checker("hello", "bello"))
    # Test case 5: True
    print(string_permutation_checker("", ""))
    # Test case 6: False
    print(string_permutation_checker("a", ""))
    # Test case 7: False
    print(string_permutation_checker("Abc", "abc"))
    # Test case 8: True
    print(string_permutation_checker("a gentleman", "elegant man"))

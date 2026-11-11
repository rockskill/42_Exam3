#!/usr/bin/env python3


"""
ASSIGNMENT:
Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.
"""


def hidenp(small: str, big: str) -> bool:
    if len(small) == 0:
        return True
    if len(small) > len(big):
        return False
    coincidence_counter: int = 0
    for i in range(len(big)):
        if big[i] == small[coincidence_counter]:
            coincidence_counter += 1
        if coincidence_counter == len(small):
            return True
    return False


if __name__ == "__main__":
    # Test case 1: True
    print(hidenp("abc", "a1b2c3"))
    # Test case 2: True
    print(hidenp("ace", "abcde"))
    # Test case 3: False
    print(hidenp("aec", "abcde"))
    # Test case 4: True
    print(hidenp("", "abc"))
    # Test case 5: False
    print(hidenp("abc", "ab"))
    # Test case 6: False
    print(hidenp("aaaa", "aaa"))
    # Test case 7: True
    print(hidenp("sing", "subsequence testing"))

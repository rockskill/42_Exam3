#!/usr/bin/env python3


def to_lower(s: str) -> str:
    lower_s: str = ""
    for c in s:
        if c == ' ':
            continue
        lower_s += c.lower()
    return lower_s


def anagram(s1: str, s2: str) -> bool:
    s1 = to_lower(s1)
    s2 = to_lower(s2)
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
    print(anagram("listen", "silent"))
    # Test case 2: True
    print(anagram("Triangle", "Integral"))
    # Test case 3: True
    print(anagram("Dormitory", "Dirty Room"))
    # Test case 4: False
    print(anagram("hello", "world"))
    # Test case 5: True
    print(anagram("", ""))
    # Test case 6: False
    print(anagram("abc", "abcc"))

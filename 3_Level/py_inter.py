#!/usr/bin/env python3


def inter(s1: str, s2: str) -> str:
    checked: set[str] = set()
    output: str = ""
    for c in s1:
        if c not in checked and c in s2:
            output += c
        checked.add(c)
    return output


if __name__ == "__main__":
    # Test case 1: "lo"
    print(inter("hello", "world"))
    # Test case 2: "ban"
    print(inter("banana", "band"))
    # Test case 3: "bc"
    print(inter("abcabc", "bc"))
    # Test case 4: ""
    print(inter("abc", "xyz"))
    # Test case 5: ""
    print(inter("", "abc"))

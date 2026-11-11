#!/usr/bin/env python3


def pattern_tracker(text: str) -> int:
    text_length: int = len(text)
    if text_length == 0:
        return 0
    pair_counter: int = 0
    for i in range(text_length - 1):
        if text[i].isdigit():
            if ord(text[i]) + 1 == ord(text[i + 1]):
                pair_counter += 1
    return pair_counter


if __name__ == "__main__":
    # Test case 1: 2
    print(pattern_tracker("123"))
    # Test case 2: 2
    print(pattern_tracker("12a34"))
    # Test case 3: 0
    print(pattern_tracker("987654321"))
    # Test case 4: 7
    print(pattern_tracker("01234567"))
    # Test case 5: 0
    print(pattern_tracker("abc"))
    # Test case 6: 0
    print(pattern_tracker("1a2b3c4"))
    # Test case 7: 2
    print(pattern_tracker("112233"))

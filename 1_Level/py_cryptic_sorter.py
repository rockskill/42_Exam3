#!/usr/bin/env python3


def get_value(string: str) -> tuple[int, str, int]:
    vowels: int = 0
    for c in string:
        if c.lower() in 'aeiou':
            vowels += 1
    return (len(string), string.lower(), vowels)


def cryptic_sorter(strings: list[str]) -> list[str]:
    strings_sorted: list[str] = list(strings)
    strings_length: int = len(strings_sorted)
    for i in range(1, strings_length):
        string: str = strings_sorted[i]
        value: tuple[int, str, int] = get_value(string)
        j: int = i - 1
        while j >= 0 and get_value(strings_sorted[j]) > value:
            strings_sorted[j + 1] = strings_sorted[j]
            j -= 1
        strings_sorted[j + 1] = string
    return strings_sorted


if __name__ == "__main__":
    # Test case 1: ["cat", "dog", "apple", "banana", "elephant"]
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    # Test case 2: ["aaa", "AAA", "bbb", "BBB"]
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    # Test case 3: ["hi", "test", "hello", "world"]
    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    # Test case 4: []
    print(cryptic_sorter([]))
    # Test case 5: [""]
    print(cryptic_sorter([""]))

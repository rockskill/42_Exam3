#!/usr/bin/env python3


"""
ASSIGNMENT:
Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.
"""


def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0 or k == 0:
        return arr
    arr_length: int = len(arr)
    k = k % arr_length
    if k == 0:
        return list(arr)
    return arr[arr_length - k:] + arr[:arr_length - k]


if __name__ == "__main__":
    # Test case 1: [4, 5, 1, 2, 3]
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    # Test case 2: [3, 1, 2]
    print(twist_sequence([1, 2, 3], 1))
    # Test case 3: [1, 2, 3, 4]
    print(twist_sequence([1, 2, 3, 4], 0))
    # Test case 4: [2, 3, 1]
    print(twist_sequence([1, 2, 3], 5))
    # Test case 5: []
    print(twist_sequence([], 3))

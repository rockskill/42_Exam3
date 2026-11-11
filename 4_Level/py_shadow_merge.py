#!/usr/bin/env python3


"""
ASSIGNMENT:
Write a function that merges two sorted lists into one sorted list.
"""


def py_shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    sorted_list: list[int] = []
    for n in list1:
        sorted_list.append(n)
    for n in list2:
        sorted_list.append(n)
    return sorted(sorted_list)


if __name__ == "__main__":
    # Test case 1: [1, 2, 3, 4, 5, 6]
    print(py_shadow_merge([1, 3, 5], [2, 4, 6]))
    # Test case 2: [1, 2, 3, 4, 5, 6]
    print(py_shadow_merge([1, 2, 3], [4, 5, 6]))
    # Test case 3: [1, 2, 3, 4]
    print(py_shadow_merge([1], [2, 3, 4]))
    # Test case 4: [1, 2, 3]
    print(py_shadow_merge([], [1, 2, 3]))
    # Test case 5: [1, 1, 1, 2, 3, 3]
    print(py_shadow_merge([1, 1, 2], [1, 3, 3]))

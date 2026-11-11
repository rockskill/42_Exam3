#!/usr/bin/env python3


"""
ASSIGNMENT:
Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.
"""


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]


if __name__ == "__main__":
    # Test case 1
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
    # Test case 2
    print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))
    # Test case 3
    print(mirror_matrix([[7]]))
    # Test case 4
    print(mirror_matrix([[1, 2, 3, 4]]))
    # Test case 5
    print(mirror_matrix([[-1, -2], [-3, -4]]))

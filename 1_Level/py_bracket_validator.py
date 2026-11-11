#!/usr/bin/env python3


def bracket_validator(s: str) -> bool:
    if len(s) == 0:
        return True
    brackets_dict: dict[str, str] = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    brackets: list[str] = []
    for c in s:
        if c == ')' or c == ']' or c == '}':
            if len(brackets) == 0:
                return False
            if c != brackets_dict[brackets.pop()]:
                return False
        elif c == '(' or c == '[' or c == '{':
            brackets.append(c)
    return len(brackets) == 0


if __name__ == '__main__':
    # Test case 1: True
    print(bracket_validator("()"))
    # Test case 2: True
    print(bracket_validator("()[]{}"))
    # Test case 3: False
    print(bracket_validator("(]"))
    # Test case 4: False
    print(bracket_validator("([)]"))
    # Test case 5: True
    print(bracket_validator("{[]}"))
    # Test case 6: True
    print(bracket_validator("hello(world)"))
    # Test case 7: False
    print(bracket_validator("((())"))
    # Test case 8: True
    print(bracket_validator(""))

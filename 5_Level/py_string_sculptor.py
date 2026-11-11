#!/usr/bin/env python3


def string_sculptor(text: str) -> str:
    if len(text) == 0:
        return ""
    sculpted_string: str = ""
    c_lower: bool = True
    for c in text:
        if c.isalpha():
            if c_lower:
                sculpted_string += c.lower()
            else:
                sculpted_string += c.upper()
            c_lower = not c_lower
        else:
            sculpted_string += c
    return sculpted_string


if __name__ == "__main__":
    # Test case 1: "hElLo"
    print(string_sculptor("hello"))
    # Test case 2: "hElLo WoRlD"
    print(string_sculptor("Hello World"))
    # Test case 3: " hElLo "
    print(string_sculptor(" hello "))
    # Test case 4: "aBc123DeF"
    print(string_sculptor("abc123def"))
    # Test case 5: "pYtHoN3.9!"
    print(string_sculptor("Python3.9!"))
    # Test case 6: ""
    print(string_sculptor(""))

#!/usr/bin/env python3


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (from_base >= 2 and from_base <= 36 and
            to_base >= 2 and to_base <= 36):
        return "ERROR"
    try:
        number_int: int = int(number, from_base)
    except ValueError:
        return "ERROR"
    if number_int == 0:
        return "0"
    number_converted: str = ""
    number_negative: bool = number_int < 0
    number_int = abs(number_int)
    base_symbols: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while number_int > 0:
        number_converted += base_symbols[number_int % to_base]
        number_int //= to_base
    if number_negative:
        number_converted += "-"
    return number_converted[::-1]


if __name__ == "__main__":
    # Test case 1: 10
    print(number_base_converter("1010", 2, 10))
    # Test case 2: 255
    print(number_base_converter("FF", 16, 10))
    # Test case 3: FF
    print(number_base_converter("255", 10, 16))
    # Test case 4: 1111011
    print(number_base_converter("123", 10, 2))
    # Test case 5: 35
    print(number_base_converter("Z", 36, 10))
    # Test case 6: Z
    print(number_base_converter("35", 10, 36))
    # Test case 7: ERROR
    print(number_base_converter("123", 1, 10))
    # Test case 8: ERROR
    print(number_base_converter("G", 16, 10))

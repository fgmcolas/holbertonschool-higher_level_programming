#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    current_value = 0
    next_value = 0
    for letter in reversed(roman_string):
        value = number[letter]
        if value < next_value:
            current_value -= value
        else:
            current_value += value
        next_value = value
    return current_value

#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    if not roman_string or type(roman_string) is not str:
        return 0

    total = 0
    previous = 0
    for roman in reversed(roman_string):
        current = roman_numerals[roman]
        if current < previous:
            total -= current
        else:
            total += current
        previous = current
    return total

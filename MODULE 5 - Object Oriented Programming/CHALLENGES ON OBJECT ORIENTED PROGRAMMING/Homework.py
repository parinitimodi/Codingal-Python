def int_to_roman(num):
    """
    Converts an integer to its Roman numeral representation.

    Args:
        num: The integer to convert.

    Returns:
        The Roman numeral representation of the integer.
    """
    roman_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    roman_numeral = ''
    for value, symbol in sorted(roman_map.items(), key=lambda item: item[0], reverse=True):
        if num >= value:
            roman_numeral += symbol * (num // value)
            num %= value
    return roman_numeral
number = 3994
roman_numeral = int_to_roman(number)
print(f"The Roman numeral representation of {number} is {roman_numeral}")

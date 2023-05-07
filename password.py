from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def create_new(length: int, values: list) -> str:
    result = ""
    char = ""

    if not values or (len(values) == 1 and 'Startswith letter' in values):
        return ""

    characters_dict = {
        '0-9': digits,
        'a-z': ascii_lowercase,
        'A-Z': ascii_uppercase,
        '@#$%': punctuation,
        'Startswith letter': ''
    }

    possible_values = ''
    for value in values:
        possible_values += ''.join(characters_dict[value])

    if "Startswith letter" in values:
        char = random.choice(characters_dict['a-z'])
        length -= 1

    for _ in range(length):
        result += ''.join(random.choice(possible_values))

    result = char + result
    return result

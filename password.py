from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def create_new(length: int, values: list) -> str:
    if not values or (len(values) == 1 and 'Startswith letter' in values):
        return ""

    characters_dict = {
        '0-9': digits,
        'a-z': ascii_lowercase,
        'A-Z': ascii_uppercase,
        '@#$%': punctuation,
    }

    char_groups = [characters_dict[v] for v in values if v in characters_dict]

    if not char_groups:
        return ""

    if "Startswith letter" in values:
        first_char = random.choice(ascii_lowercase)
        length -= 1
    else:
        first_char = ""

    password_chars = [random.choice(group) for group in char_groups]

    all_chars = "".join(char_groups)
    password_chars += random.choices(all_chars, k=length - len(password_chars))

    random.shuffle(password_chars)
    return first_char + "".join(password_chars)

import random


def generate_password(use_upper, use_lower, use_digits, use_symbols):
    """Generates a user password"""
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    symbols = '$#&'

    all_letters = ""

    if use_upper:
        all_letters += uppercase_letters

    if use_lower:
        all_letters += lowercase_letters

    if use_digits:
        all_letters += digits

    if use_symbols:
        all_letters += symbols

    return "".join((random.sample(all_letters, password_length)))


if __name__ == "__main__":
    print("Starting Script")
    password_length = 8
    passwords_to_generate = 3
    include_upper, include_lower, include_digits, include_symbols = True, True, True, False

    for x in range(passwords_to_generate):
        new_password = generate_password(include_upper, include_lower, include_digits, include_symbols)
        print(f'{x} - {new_password}')

    print("Ending Script")


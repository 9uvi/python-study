import string
import random

def generate_password(no_characters: int) -> str:
    """
    Return a password with "no_characters" characters.

    Args:
        no_characters (int): Length of the password.

    Returns:
        password (str): Generated password.
    """

    if no_characters < 12:
        no_characters = 12

    spec_chars = "~!@#$%^&*()_+"
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(lowercase_letters)
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    lowercase_count = no_characters - 2

    password = str(random.choice(uppercase_letters))
    password += str(random.choice(digits))
    password += str(random.choice(spec_chars))
    password += "".join(lowercase_letters[:lowercase_count - 1])

    return password


if __name__ == "__main__":
    assert len(generate_password(8)) == 12
    pw = generate_password(14)
    assert len(pw) == 14
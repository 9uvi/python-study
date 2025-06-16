import string

def rot13(text: str) -> str:
    """
    Encrypt the text using ROT13 protocol.

    Args:
        text (str): Text to be encrypted.

    Returns:
        enc_text (str): The encrypted text.
    """

    enc_text = ""

    for char in text:
        if char in string.ascii_lowercase:
            # Get its index
            char_idx = string.ascii_lowercase.find(char)
            enc_text += string.ascii_lowercase[(char_idx + 13) % 26]
        elif char in string.ascii_uppercase:
            # Get its index
            char_idx = string.ascii_uppercase.find(char)
            enc_text += string.ascii_uppercase[(char_idx + 13) % 26]
        else:
            enc_text += char

    return enc_text


if __name__ == "__main__":
    assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
    assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
    assert rot13(rot13('Hello, world!')) == 'Hello, world!'
    assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
    assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
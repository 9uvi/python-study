import string

def get_uppercase(text: str) -> str:
    """
    Return the uppercase version of the given argument.

    Args:
        text (str): Text to be uppercased.

    Returns:
        new_text (str): Uppercase string.
    """

    if not text:
        return ''

    new_text = ""

    for char in text:
        if char in string.ascii_lowercase:
            new_text += chr(ord(char) - 32)
        else:
            new_text += char

    return new_text

if __name__ == "__main__":
    assert get_uppercase('Hello') == 'HELLO'
    assert get_uppercase('hello') == 'HELLO'
    assert get_uppercase('HELLO') == 'HELLO'
    assert get_uppercase('Hello, world!') == 'HELLO, WORLD!'
    assert get_uppercase('goodbye 123!') == 'GOODBYE 123!'
    assert get_uppercase('12345') == '12345'
    assert get_uppercase('') == ''
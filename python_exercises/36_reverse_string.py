def reverse_string(string: str) -> str:
    """
    Return the argument string, but reversed.

    Args:
        string (str): String to be reversed.

    Returns:
        rev_string (str): Reversed string.
    """

    reverse_string = ""
    # reverse_string = string[::-1]

    list_of_chars = list(string)

    for char in list_of_chars[::-1]:
        reverse_string += char

    return reverse_string

if __name__ == "__main__":
    assert reverse_string('Hello') == 'olleH'
    assert reverse_string('') == ''
    assert reverse_string('aaazzz') == 'zzzaaa'
    assert reverse_string('xxxx') == 'xxxx'
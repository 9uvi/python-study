def get_title_case(text: str) -> str:
    """
    Makes the first letter of every word uppercase.
    Words can also be separated by non alpha characters, not only spaces.

    Args:
        text (str): Text to be title cased.

    Returns:
        titled_str (str): Result string
    """

    titled_str = ""

    if text == titled_str:
        return titled_str
    
    titled_str = text[0].upper()

    i = 1
    
    while i < len(text):
        if not text[i].isalpha():
            for j in range(i ,len(text)):
                if text[j].isalpha():
                    titled_str += text[j].upper()
                    i = j
                    break
                else:
                    titled_str += text[j]

        else:
            titled_str += text[i].lower()

        i += 1

    return titled_str

if __name__ == "__main__":
    assert get_title_case('Hello, world!') == 'Hello, World!'
    assert get_title_case('HELLO') == 'Hello'
    assert get_title_case('hello') == 'Hello'
    assert get_title_case('hElLo') == 'Hello'
    assert get_title_case('') == ''
    assert get_title_case('abc123xyz') == 'Abc123Xyz'
    assert get_title_case('cat dog RAT') == 'Cat Dog Rat'
    assert get_title_case('cat,dog,RAT') == 'Cat,Dog,Rat'
def find_and_replace(string: str, old_word: str, new_word: str):
    """
    Replace the second argument "old_world" with the third "new_word" in the text from the first argument "string".

    Params:
        string (str): Text to be searched in.
        old_word (str): Term to be searched.
        new_word (str): Term to be replaced with.
    """

    while True:
        if old_word in string:
            string = string.replace(old_word, new_word)
        else: 
            break

    return string

if __name__ == "__main__":
    assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
    assert find_and_replace('fox', 'fox', 'dog') == 'dog'
    assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
    assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
    assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
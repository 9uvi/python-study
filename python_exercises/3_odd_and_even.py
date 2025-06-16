"""
Write two functions to check whether a number is odd or even.
"""

def is_odd(number):
    """
    Returns True if the argument is odd, returns False otherwise.

    Params:
        number (int): The number that will be checked for parity.
    """

    return number % 2 == 1


def is_even(number):
    """
    Returns True if the argument is even, returns False otherwise.

    Params:
        number (int): The number that will be checked for parity.
    """

    return number % 2 == 0

if __name__ == "__main__":
    assert is_odd(42) == False
    assert is_odd(9999) == True
    assert is_odd(-10) == False
    assert is_odd(-11) == True
    assert is_odd(3.1415) == False
    assert is_even(42) == True
    assert is_even(9999) == False
    assert is_even(-10) == True
    assert is_even(-11) == False
    assert is_even(3.1415) == False
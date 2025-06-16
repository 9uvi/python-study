def is_even(n: int) -> bool:
    """
    Returns whether n is even without using multiplication, division or modulo operators.

    Args:
        n (int): Number to be checked.
    
    Returns:
        True is n is even.
        False if n is odd.
    """

    return n & 1 == 0

if __name__ == "__main__":
    # Test cases for is_even
    assert is_even(10) == True, "Test Case 1 Failed: 10 should be even"
    assert is_even(0) == True, "Test Case 2 Failed: 0 should be even"
    assert is_even(-2) == True, "Test Case 3 Failed: -2 should be even"
    assert is_even(13) == False, "Test Case 4 Failed: 13 should not be even"
    assert is_even(-7) == False, "Test Case 5 Failed: -7 should not be even"
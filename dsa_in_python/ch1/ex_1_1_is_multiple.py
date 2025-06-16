def is_multiple(n: int, m: int) -> bool:
    """
    Returns true if n is multiple of m.

    Args:
        n (int): Possible multiple.
        m (int): Number to test the possible multiple against.

    Returns:
        True if n % m == 0
        False if n % m != 0
    """

    return n % m == 0


if __name__ == "__main__":
    # Test cases where the result should be True
    assert is_multiple(10, 5) == True, "Test Case 1 Failed: 10 should be a multiple of 5"
    assert is_multiple(100, 10) == True, "Test Case 2 Failed: 100 should be a multiple of 10"
    assert is_multiple(0, 5) == True, "Test Case 3 Failed: 0 should be a multiple of any non-zero number"
    assert is_multiple(-10, 5) == True, "Test Case 4 Failed: -10 should be a multiple of 5"
    assert is_multiple(-10, -5) == True, "Test Case 5 Failed: -10 should be a multiple of -5"
    assert is_multiple(10, -5) == True, "Test Case 6 Failed: 10 should be a multiple of -5"
    assert is_multiple(7, 1) == True, "Test Case 7 Failed: Any integer is a multiple of 1"
    assert is_multiple(-7, 1) == True, "Test Case 8 Failed: Any negative integer is a multiple of 1"
    assert is_multiple(3, 3) == True, "Test Case 9 Failed: A number is a multiple of itself"

    # Test cases where the result should be False
    assert is_multiple(10, 3) == False, "Test Case 10 Failed: 10 should not be a multiple of 3"
    assert is_multiple(7, 2) == False, "Test Case 11 Failed: 7 should not be a multiple of 2"
    assert is_multiple(-10, 3) == False, "Test Case 12 Failed: -10 should not be a multiple of 3"
    assert is_multiple(10, -3) == False, "Test Case 13 Failed: 10 should not be a multiple of -3"

    # Test for ZeroDivisionError (optional, but good practice)
    try:
        is_multiple(10, 0)
    except ZeroDivisionError:
        print("Successfully caught ZeroDivisionError for Test Case 14.")
    else:
        assert False, "Test Case 14 Failed: Should have raised ZeroDivisionError"
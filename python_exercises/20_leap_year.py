def is_leap_year(year: int) -> bool:
    """
    Returns True if the "year" argument is a leap year, False otherwise.

    Args:
        year (int): Year to be checked if leap.

    Returns:
        bool
    """

    if not year % 4: 
        if not year % 400:
            return True
        elif not year % 100:
            return False
        else:
            return True
    
    return False

if __name__ == "__main__":
    assert is_leap_year(1999) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(2001) is False
    assert is_leap_year(2004) is True
    assert is_leap_year(2100) is False
    assert is_leap_year(2400) is True
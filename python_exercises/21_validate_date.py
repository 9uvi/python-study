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

def is_valid_date(year: int, month: int, day: int) -> bool:
    """
    Return a boolean represending the validity of the argument date.

    Args:
        year (int): Given year.
        month (int): Given month.
        day (int): Given day.

    Returns:
        bool
    """

    if is_leap_year(year):
        if month == 2:
            return 1 <= day <= 29
    else:
        if month == 2:
            return 1 <= day <= 28
    
    months_with_30 = [4, 6, 9, 11]

    last_day = 30 if month in months_with_30 else 31

    return year > 0 and (1 <= month <= 12) and (1 <= day <= last_day)

if __name__ == "__main__":
    assert is_valid_date(1999, 12, 31) == True
    assert is_valid_date(2000, 2, 29) == True
    assert is_valid_date(2001, 2, 29) == False
    assert is_valid_date(2029, 13, 1) == False
    assert is_valid_date(1000000, 1, 1) == True
    assert is_valid_date(2015, 4, 31) == False
    assert is_valid_date(1970, 5, 99) == False
    assert is_valid_date(1981, 0, 3) == False
    assert is_valid_date(1666, 4, 0) == False

    import datetime
    d = datetime.date(1970, 1, 1)
    oneDay = datetime.timedelta(days=1)
    for i in range(1000000):
        assert is_valid_date(d.year, d.month, d.day) == True
        d += oneDay
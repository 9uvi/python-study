def ordinal_suffix(number: int) -> str:
    suffixes = ["st", "nd", "rd"]

    if number % 100 in [11, 12, 13]:
        return f"{number}th"
    elif number % 10 in [1, 2, 3]:
        return f"{number}{suffixes[(number % 10) - 1]}"
    else:
        return f"{number}th"
    

if __name__ == "__main__":
    assert ordinal_suffix(0) == '0th'
    assert ordinal_suffix(1) == '1st'
    assert ordinal_suffix(2) == '2nd'
    assert ordinal_suffix(3) == '3rd'
    assert ordinal_suffix(4) == '4th'
    assert ordinal_suffix(10) == '10th'
    assert ordinal_suffix(11) == '11th'
    assert ordinal_suffix(12) == '12th'
    assert ordinal_suffix(13) == '13th'
    assert ordinal_suffix(14) == '14th'
    assert ordinal_suffix(15) == '15th'
    assert ordinal_suffix(101) == '101st'
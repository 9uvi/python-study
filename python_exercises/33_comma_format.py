def comma_format(number: int | float) -> str:
    """
    Return a comma formatted number.

    Args:
        number (int): Number to be comma formatted.
    """

    result = ""

    string_number = str(number)

    has_dot = True if '.' in string_number else False

    count = 1

    if has_dot:
        split_string = string_number.split('.')


        for char in split_string[0][::-1]:
            result += char
            if not count % 3:
                result += ","
            count += 1

        return result[::-1] + '.' + split_string[1]


    for char in string_number[::-1]:
        result += char
        if not count % 3 and char == string_number[len(string_number) - 1]:
            result += ","
        count += 1

    return result[::-1]


if __name__ == "__main__":
    assert comma_format(1) == '1'
    assert comma_format(10) == '10'
    assert comma_format(100) == '100'
    assert comma_format(1000) == '1,000'
    assert comma_format(10000) == '10,000'
    assert comma_format(100000) == '100,000'
    assert comma_format(1000000) == '1,000,000'
    assert comma_format(1234567890) == '1,234,567,890'
    assert comma_format(1000.123456) == '1,000.123456'

def convert_str_to_int(string: str) -> int:
    """
    Converts the string argument to integer.

    Args:
        string (str): Argument string that will be casted to int.
    """

    DIGITS_STR_TO_INT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    negative = True if string[0] == "-" else False

    new_str = string

    if negative:
        new_str = string[1:]

    my_num = int(new_str[0])

    for i in range(1, len(new_str)):
        my_num *= 10
        my_num += DIGITS_STR_TO_INT[new_str[i]]
    
    return my_num if not negative else -my_num

if __name__ == "__main__":
    for i in range(-10000, 10000):
        assert convert_str_to_int(str(i)) == i
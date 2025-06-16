def convert_int_to_str(number: int) -> str:
    """
    Convert the given integer argument "number" into a string.

    Args:
        number (int): Number to be converted to string.

    Returns:
        number_str (str): String version of the argument number.
    """

    if number == 0:
        return '0'

    digits = "0123456789"

    number_str = ""

    negative = True if number < 0 else False

    if negative:
        number *= -1

    while number > 0:
        number_str += digits[number % 10]
        number = number // 10

    return "-" + number_str[::-1] if negative else number_str[::-1]

if __name__ == "__main__":
    for i in range(-10000, 10000):
        assert convert_int_to_str(i) == str(i)
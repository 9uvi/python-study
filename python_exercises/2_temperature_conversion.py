"""
Write a function called convert_to_fahrenheit with a degrees_celsius param.
Write a function called convert_to_celsius with a degrees_fahrenheit param.
"""

def convert_to_fahrenheit(degrees_celsius):
    """
    Converts degrees celsius to degrees fahrenheit using formula:
        fahrenheit = celsius x (9 / 5) + 32

    Params:
        degrees_celsius (float): Celsius degrees to be converted.
    """

    return degrees_celsius * (9 / 5) + 32

def convert_to_celsius(degrees_fahrenheit):
    """
    Converts degrees fahrenheit to degrees celsius using formula:
        celsius = (fahrenheit - 32) x (5 / 9)

    Params:
        degrees_fahrenheit (float): Fahrenheit degrees to be converted.
    """

    return (degrees_fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    assert convert_to_fahrenheit(0) == 32
    assert convert_to_fahrenheit(100) == 212
    assert convert_to_celsius(0) == -17.77777777777778
    assert convert_to_celsius(180) == 82.22222222222223
    assert convert_to_celsius(convert_to_fahrenheit(15)) == 15

    # Rounding errors cause a slight discrepancy:
    assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001
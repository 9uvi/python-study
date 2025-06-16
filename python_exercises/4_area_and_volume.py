"""
Write four functions that compute the area, perimeter, volume and surface area.
"""

def area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle with sides length and width.
    
    area = width * height

    Params:
        length (float): lenght of the rectangle.
        width (float): width of the rectangle.
    """

    return length * width

def perimeter(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle with given arguments for length and width.

    perimeter = 2 * length + 2 * width

    Params:
        length (float): lenght of the rectangle.
        width (float): width of the rectangle.
    """

    return 2 * length + 2 * width

def volume(length: float, width: float, height: float) -> float:
    """
    Calculates the volume of the rectangular parallelipiped with given arguments.

    volume = length * width * height

    Params:
        length (float): lenght of the parallelipiped.
        width (float): width of the parallelipiped.
        height (float): height of the parallelipiped.
    """

    return length * width * height


def surface_area(length: float, width: float, height: float) -> float:
    """
    Calculates the surface area of the rectangular parallelipiped with given arguments.

    surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)

    Params:
        length (float): lenght of the parallelipiped.
        width (float): width of the parallelipiped.
        height (float): height of the parallelipiped.
    """

    return 2 * (width * height) + 2 * (length * width) + 2 * (length * height)

if __name__ == "__main__":
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) == 199960002
    assert surface_area(5, 8, 10) == 340
def draw_pyramid(height: int) -> None:
    """
    Draw a pyramid.

    Args:
        height (int): Height of the pyramid.
    """

    width = 1

    for i in range(height):
        to_print = "#" * width
        centered = to_print.center(height * 2 - 1)

        print(centered)

        width += 2

if __name__ == "__main__":
    draw_pyramid(8)
def draw_border(width: int, height: int) -> None:
    """
    Draw the border of a rectangle with size width x height.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

    Returns:
        None
    """

    if width < 2 or height < 2:
        return

    end_row = f"+{'-' * (width - 2)}+"

    print(end_row)

    for _ in range(height - 2):
        print("|", " " * (width - 4), "|")

    print(end_row)

if __name__ == "__main__":
    draw_border(2, 2)
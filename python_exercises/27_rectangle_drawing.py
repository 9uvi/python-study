def draw_rectangle(width: int, height: int) -> None:
    """
    Draw a solid rectangle made of "#" with size width x height.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    
    Returns:
        None
    """

    for _ in range(height):
        print("#" * width)

if __name__ == "__main__":
    draw_rectangle(10, 5)
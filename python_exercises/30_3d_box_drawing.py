def draw_box(size: int) -> None:
    """
    Print a box.

    Args:
        size (int): Size of the box.
    """

    left_spaces = size
    right_spaces = 0

    print(f"{' ' * (left_spaces + 1)}+{'-' * size * 2}+")

    for _ in range(size):
        print(f"{' ' * left_spaces}/{' ' * size * 2}/{' ' * right_spaces}|")
        left_spaces -= 1
        right_spaces += 1

    print(f"+{'-' * size * 2}+{' ' * size}+")

    right_spaces = size - 1

    for _ in range(size):
        print(f"{'|'}{' ' * size * 2}|{' ' * right_spaces}/")
        right_spaces -= 1

    print(f"+{'-' * size * 2}+")


if __name__ == "__main__":
    draw_box(13)
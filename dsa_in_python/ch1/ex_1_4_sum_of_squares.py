def sum_squares_less_than(n: int) -> int:
    """
    Return the sum of the squares of all the positive integers less than n.

    Args:
        n (int): Upper limit.

    Returns:
        sum_of_squares (int): Sum of the squares.
    """

    if n <= 0:
        return 0

    n = n - 1

    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6

    return sum_of_squares


if __name__ == "__main__":
    assert sum_squares_less_than(4) == 14
    assert sum_squares_less_than(1) == 0
    assert sum_squares_less_than(2) == 1
    assert sum_squares_less_than(3) == 5
    assert sum_squares_less_than(10) == 285
    assert sum_squares_less_than(0) == 0
    assert sum_squares_less_than(-5) == 0
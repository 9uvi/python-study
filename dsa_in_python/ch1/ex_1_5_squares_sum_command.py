def squares_sum(n: int) -> int:
    """
    Squares sum using a list comprehension.

    Args:
        n (list): Up to which number to sum.
    
    Returns:
        Returns the sum of the squares.
    """

    squares = [i**2 for i in range(n)]

    return sum(squares)

if __name__ == "__main__":
    assert squares_sum(4) == 14
    assert squares_sum(1) == 0
    assert squares_sum(2) == 1
    assert squares_sum(3) == 5
    assert squares_sum(10) == 285
    assert squares_sum(0) == 0
    assert squares_sum(-5) == 0
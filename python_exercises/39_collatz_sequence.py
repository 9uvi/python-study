def collatz(number: int) -> list:
    """
    Return the Collatz sequence down from argument "number".

    Args:
        number (int): Start point of Collatz sequence.
    
    Returns:
        collatz_seq (list): The Collatz sequence from number to 1.
    """

    if number == 0:
        return []

    collatz_seq = []

    while number != 1:
        collatz_seq.append(number)

        if not number % 2:
            number //= 2
        else:
            number = 3 * number + 1

    collatz_seq.append(1)

    return collatz_seq


if __name__ == "__main__":
    assert collatz(0) == []
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert len(collatz(256)) == 9
    assert len(collatz(257)) == 123

    import random
    random.seed(42)
    
    for i in range(1000):
        startingNum = random.randint(1, 10000)
        seq = collatz(startingNum)
        assert seq[0] == startingNum # Make sure it includes the starting number.
        assert seq[-1] == 1 # Make sure the last integer is 1.
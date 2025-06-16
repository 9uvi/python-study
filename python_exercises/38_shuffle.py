import random

def shuffle(numbers: list) -> None:
    """
    Shuffle the given numbers list and return it.

    Args:
        numbers (list): Numbers to be shuffled.
    
    Returns:
        shuffled_numbers (list): The shuffled numbers.
    """

    for _ in range(len(numbers)):
        r1 = random.randint(0, len(numbers) - 1)
        r2 = random.randint(0, len(numbers) - 1)
        numbers[r1], numbers[r2] = numbers[r2], numbers[r1]


if __name__ == "__main__":
    random.seed(42)
    # Perform this test ten times:
    for i in range(10):
        testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(testData1)
        # Make sure the number of values hasn't changed:
        assert len(testData1) == 10
        # Make sure the order has changed:
        assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Make sure that when re-sorted, all the original values are there:
        assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

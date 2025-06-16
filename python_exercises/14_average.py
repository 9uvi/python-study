def average(numbers: list[int]) -> int:
    """
    Compute and return the average of the given argument list.

    Params:
        numbers: (list[int])
    """

    my_sum = 0

    for number in numbers:
        my_sum += number

    return my_sum // len(numbers)

if __name__ == "__main__":
    assert average([1, 2, 3]) == 2
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert average([12, 20, 37]) == 23
    assert average([0, 0, 0, 0, 0]) == 0
    import random
    random.seed(42)
    testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for i in range(1000):
        random.shuffle(testData)
        assert average(testData) == 2
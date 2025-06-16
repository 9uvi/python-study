def median(numbers: list[int]) -> int | float | None:
    """
    Return the median from the given argument list.

    Params:
        numbers: (list[int]): List of integers on which to find the median.
    """

    if not len(numbers):
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    parity = length % 2

    if not parity:
        return (sorted_numbers[length // 2] + sorted_numbers[length // 2 - 1]) / 2
    
    return sorted_numbers[length // 2]

    
if __name__ == "__main__":
    assert median([]) == None
    assert median([1, 2, 3]) == 2
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
    import random
    random.seed(42)
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    for i in range(1000):
        random.shuffle(testData)
        assert median(testData) == 6    


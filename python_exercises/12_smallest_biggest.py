def get_smallest(numbers: list[int]) -> int | None:
    if len(numbers) == 1:
        return numbers[0]

    if not numbers:
        return None

    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    
    return smallest

if __name__ == "__main__":
    assert get_smallest([1, 2, 3]) == 1
    assert get_smallest([3, 2, 1]) == 1
    assert get_smallest([28, 25, 42, 2, 28]) == 2
    assert get_smallest([1]) == 1
    assert get_smallest([]) == None
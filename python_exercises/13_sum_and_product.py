def calculate_sum(numbers: list[int]) -> int:
    """
    Returns the sum of all the numbers from the argument list.

    Params:
        numbers (list[int]): List of numbers to be summed.
    """
    my_sum = 0

    if not len(numbers):
        return my_sum
    
    for number in numbers:
        my_sum += number

    return my_sum

def calculate_product(numbers: list[int]) -> int:
    """
    Returns the product of all of the numbers from the argument list.

    Params:
        numbers (list[int]): List of numbers to be multiplied together.
    """

    my_product = 1

    if not len(numbers):
        return my_product
    
    for number in numbers:
        my_product *= number

    return my_product

if __name__ == "__main__":
    assert calculate_sum([]) == 0
    assert calculate_sum([2, 4, 6, 8, 10]) == 30
    assert calculate_product([]) == 1
    assert calculate_product([2, 4, 6, 8, 10]) == 3840
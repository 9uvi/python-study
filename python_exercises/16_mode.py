def mode(numbers: list[int]) -> int | None:
    """
    Find and return the mode of the given argument list.

    Params:
        numbers (list[int]): Number list to be computed for mode.
    """

    if not numbers:
        return None
    
    my_keys = set(numbers)
    my_dict = dict.fromkeys(my_keys, 0)

    for number in numbers:
        my_dict[number] += 1
    
    return max(my_dict, key=my_dict.get)
    

if __name__ == "__main__":
    assert mode([]) == None
    assert mode([1, 1, 2, 3, 4]) == 1
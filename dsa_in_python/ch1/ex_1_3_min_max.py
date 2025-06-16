def get_min_max(l: list) -> tuple | None:
    """
    Return a tuple of the form (min, max) with the min and max item from the list.

    Args:
        l (list): List of searched items.
    
    Returns:
        min_max_tuple (tuple): The (min, max) solution.
    """

    if not l:
        return None

    mini, maxi = l[0], l[0]

    for item in l:
        if item < mini:
            mini = item
        
        if item > maxi:
            maxi = item

    return mini, maxi

if __name__ == "__main__":
    assert get_min_max([4, 7, 1, 9, 3, 5]) == (1, 9)
    assert get_min_max([-5, 10, 0, -12, 3]) == (-12, 10)
    assert get_min_max([3.14, 1.618, -0.5, 2.718]) == (-0.5, 3.14)
    assert get_min_max([100, 25.5, -50, 99.9, -50.1]) == (-50.1, 100)
    assert get_min_max([8, 2, 6, 2, 8, 8]) == (2, 8)
    assert get_min_max([7, 7, 7, 7]) == (7, 7)
    assert get_min_max([42, -42]) == (-42, 42)
    assert get_min_max([100]) == (100, 100)
    assert get_min_max(["apple", "zebra", "banana", "kiwi"]) == ("apple", "zebra")
    assert get_min_max([]) == None
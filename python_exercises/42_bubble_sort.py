def bubble_sort(l: list) -> list:
    """
    Sort the list l in-place, using the Bubble Sort algorithm.

    Args:
        l (list): List to be sorted.
    
    Returns:
        None
    """

    length = len(l)

    for i in range(0, length):
        for j in range(i, length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    return l
    

if __name__ == "__main__":
    assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
    assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]
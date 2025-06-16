def merge_two_lists(l1: list, l2: list) -> list:
    """
    Merge two sorted lists and keep the new list sorted.

    Args:
        l1 (list): First list
        l2 (list): Second list

    Returns:
        merged_list (list): Merged, sorted list
    """

    if not l1 and l2:
        return l2
    elif not l2 and l1:
        return l1

    merged_list = []
    c1 = 0
    c2 = 0
    len1 = len(l1)
    len2 = len(l2)

    while c1 < len1 and c2 < len2:
        if l1[c1] < l2[c2]:
            merged_list.append(l1[c1])
            c1 += 1
        elif l1[c1] > l2[c2]:
            merged_list.append(l2[c2])
            c2 += 1
        else:
            merged_list.append(l1[c1])
            merged_list.append(l2[c2])
            c1 += 1
            c2 += 1

    if c1 < len1:
        merged_list.extend(l1[c1:])
    elif c2 < len2:
        merged_list.extend(l2[c2:])
    
    return merged_list


if __name__ == "__main__":
    assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
    assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
    assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
    assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]
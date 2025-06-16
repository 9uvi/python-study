def make_change(amount: int) -> dict:
    """
    Take a number and divide it into change.

    Args:
        amount (int): Amount to be changed.
    
    Returns:
        change_result (dict): Dictionary of change.
    """

    change = {
        "quarters": 25,
        "dimes": 10,
        "nickels": 5,
        "pennies": 1,
    }

    change_result = dict()

    for key, value in change.items():
        while amount - value >= 0:
            if key not in change_result.keys():
                change_result[key] = 0
            change_result[key] += 1
            amount -= value
    
    return change_result

if __name__ == "__main__":
    assert make_change(30) == {'quarters': 1, 'nickels': 1}
    assert make_change(10) == {'dimes': 1}
    assert make_change(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
    assert make_change(100) == {'quarters': 4}
    assert make_change(125) == {'quarters': 5}
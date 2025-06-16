def roll_dice(number_of_dice: int) -> int:
    """
    Roll "number_of_dice" D6 dices and return their sum.

    Args:
        number_of_dice (int): Number of dice to be rolled and summed.

    Returns:
        sum_of_dice (int): The sum of the rolled dice.
    """

    import random

    if number_of_dice == 0:
        return 0
    
    dice = [random.randint(1, 6) for _ in range(number_of_dice)]

    sum_of_dice = sum(dice)

    return sum_of_dice


if __name__ == "__main__":
    assert roll_dice(0) == 0
    assert roll_dice(1000) != roll_dice(1000)
    for i in range(1000):
        assert 1 <= roll_dice(1) <= 6
        assert 2 <= roll_dice(2) <= 12
        assert 3 <= roll_dice(3) <= 18
        assert 100 <= roll_dice(100) <= 600
def get_cost_of_coffee(no_coffees: int, coffee_price: float) -> float:
    """
    Get the total cost for no_coffees when the 8th is free.

    Args:
        no_coffees (int): Number of coffees.
        coffee_price (float): Price of a coffee.

    Returns:
        total_price (float): The total price for n coffees, at x price with the 8th coffee free discount.
    """

    if no_coffees == 0:
        return 0
    
    divmod_tuple = divmod(no_coffees, 8)
    total_price = (no_coffees * coffee_price) - (divmod_tuple[0] * coffee_price)

    if not divmod_tuple[1]:
        total_price += coffee_price

    return total_price

if __name__ == "__main__":
    assert get_cost_of_coffee(7, 2.50) == 17.50
    assert get_cost_of_coffee(8, 2.50) == 20
    assert get_cost_of_coffee(9, 2.50) == 20
    assert get_cost_of_coffee(10, 2.50) == 22.50    
    for i in range(1, 4):
        assert get_cost_of_coffee(0, i) == 0
        assert get_cost_of_coffee(8, i) == 8 * i
        assert get_cost_of_coffee(9, i) == 8 * i
        assert get_cost_of_coffee(18, i) == 16 * i
        assert get_cost_of_coffee(19, i) == 17 * i
        assert get_cost_of_coffee(30, i) == 27 * i
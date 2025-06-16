def print_handshakes(people: list) -> int:
    """
    Write the handshakes between the people and return their count.

    Args:
        people (list): List of people that shake hands.
    
    Returns:
        handshakes_count (int): How many handshakes took place.
    """

    if not people:
        return 0
    
    people_length = len(people)
    handshakes = (people_length * (people_length - 1)) // 2
    
    for i in range(people_length - 1):
        for j in range(i, people_length):
            print(f"{people[i]} shakes hands with {people[j]}")

    return handshakes


if __name__ == "__main__":
    assert print_handshakes(['Alice', 'Bob']) == 1
    assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
    assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
def fizz_buzz(up_to: int) -> None:
    """
    FizzBuzz game.

    Params:
        up_to (int): Up to what number should the iterations go.
    """

    for i in range(1, up_to + 1):
        if not (i % 3) and not (i % 5):
            print("FizzBuzz")
        elif not (i % 3):
            print("Fizz")
        elif not (i % 5):
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizz_buzz(15)
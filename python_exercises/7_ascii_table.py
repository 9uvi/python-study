def print_ASCII_table() -> None:
    """
    Prints all the ASCII numbers and corresponding character from 32 to 126.
    """

    for i in range(32, 127):
        print(f"{i} {chr(i)}")

if __name__ == "__main__":
    print_ASCII_table()
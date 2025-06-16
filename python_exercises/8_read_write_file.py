def write_to_file(filename: str, text: str) -> None:
    """
    Write to a file, in the same folder, with the given name.

    Params:
        filename (str): The name of the file to write to. It has to be in the same folder.
        text (str): The text to be written to the file.
    """

    with open(filename, 'w') as f:
        f.write(text)

def append_to_file(filename: str, text: str) -> None:
    """
    Append to a file, in the same folder, with the given name.

    Params:
        filename (str): The name of the file to write to. It has to be in the same folder.
        text (str): The text to be appended to the file.
    """

    with open(filename, 'a') as f:
        f.write(text)

def read_from_file(filename: str) -> None:
    """
    Reads all lines from a file, in the same folder, with the given name.

    Params:
        filename (str): The name of the file to read from. It has to be in the same folder.
    """

    with open(filename, 'r') as f:
        for line in f:
            print(line)



if __name__ == "__main__":
    write_to_file("text.txt", "What a great day.\n")
    append_to_file("text.txt", "This text was appended.\n")
    read_from_file("text.txt")
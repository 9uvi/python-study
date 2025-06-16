def get_chess_board():
    """
    Return an 8 x 8 matrix with items "black" or "white" representing a chess board.
    """

    return [['white' if (i + j) % 2 == 0 else 'black' for j in range(8)] for i in range(8)]

def get_chess_square_color(row: int, col: int) -> str:
    """
    Return the color of the square found at given row and col arguments on a chess board.

    Params:
        row (int): Chess board row.
        col (int): Chess board column.
    """

    row = row - 1
    col = col - 1

    if not (0 <= row < 8) or not (0 <= col < 8):
        return ''

    chess_board = get_chess_board()

    return chess_board[row][col]

if __name__ == "__main__":
    assert get_chess_square_color(1, 1) == 'white'
    assert get_chess_square_color(2, 1) == 'black'
    assert get_chess_square_color(1, 2) == 'black'
    assert get_chess_square_color(8, 8) == 'white'
    assert get_chess_square_color(0, 8) == ''
    assert get_chess_square_color(2, 9) == ''
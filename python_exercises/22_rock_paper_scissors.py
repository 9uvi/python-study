def rps_winner(player1: str, player2: str) -> str:
    """
    Chooses a winner for Rock, Paper, Scissors based on the arguments.

    Args:
        player1 (str): 1st player's choice.
        player2 (str): 2nd player's choice.

    Returns:
        winner (str): Who won.
    """

    winner = 'tie'

    if player1 == player2:
        return winner

    anti_dict = {
        "anti_rock": "paper",
        "anti_paper": "scissors",
        "anti_scissors": "rock",
    }

    if player2 == anti_dict[f"anti_{player1}"]:
        winner = "player two"
    elif player1 == anti_dict[f"anti_{player2}"]:
        winner = "player one"
    
    return winner

if __name__ == "__main__":
    assert rps_winner('rock', 'paper') == 'player two'
    assert rps_winner('rock', 'scissors') == 'player one'
    assert rps_winner('paper', 'scissors') == 'player two'
    assert rps_winner('paper', 'rock') == 'player one'
    assert rps_winner('scissors', 'rock') == 'player two'
    assert rps_winner('scissors', 'paper') == 'player one'
    assert rps_winner('rock', 'rock') == 'tie'
    assert rps_winner('paper', 'paper') == 'tie'
    assert rps_winner('scissors', 'scissors') == 'tie'
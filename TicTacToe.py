"""
Program: Tic-Tac-Toe Game
Author: Xavier Chitison
Purpose: A two-player Tic-Tac-Toe game that allows players to enter
         their names, take turns placing X and O, detects winners and
         ties, keeps score, and allows multiple rounds to be played.
Resources: Python Crash Course, Chapters 1-7
Date: September 11, 2026
"""

"""
Output example:
=================================
        TIC-TAC-TOE
=================================

Player 1, enter your name: Xavier
Player 2, enter your name: Mason

Xavier = X
Mason = O

     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9

Xavier (X), choose a position: 5

     1 | 2 | 3
    ---+---+---
     4 | X | 6
    ---+---+---
     7 | 8 | 9

Mason (O), choose a position: 1

"""

def display_board(board):
    """Display the current Tic-Tac-Toe board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def display_position_guide():
    """Display the numbers players use to select board positions."""
    print("\nChoose a position using the numbers below:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def get_player_name(player_number):
    """Ask a player for a name and make sure a name is entered."""
    while True:
        name = input(f"Player {player_number}, enter your name: ").strip()

        if name:
            return name

        print("Please enter a name.")


def get_player_move(board, player_name, symbol):
    """Ask the current player for a valid board position."""
    while True:
        move = input(
            f"{player_name} ({symbol}), choose a position from 1-9: "
        ).strip()

        if not move.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(move)

        if position < 1 or position > 9:
            print("Please choose a position from 1 to 9.")
            continue

        board_index = position - 1

        if board[board_index] != " ":
            print("That position is already taken. Try again.")
            continue

        return board_index


def check_winner(board, symbol):
    """Return True when the given symbol has a winning combination."""
    winning_combinations = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for combination in winning_combinations:
        first = combination[0]
        second = combination[1]
        third = combination[2]

        if (
            board[first] == symbol
            and board[second] == symbol
            and board[third] == symbol
        ):
            return True

    return False


def check_tie(board):
    """Return True when every board position has been filled."""
    for space in board:
        if space == " ":
            return False

    return True


def display_scores(players, scores):
    """Display the current wins and tie total."""
    print("\n==============================")
    print("         GAME SCORES")
    print("==============================")
    print(f"{players['X']}: {scores['X']} win(s)")
    print(f"{players['O']}: {scores['O']} win(s)")
    print(f"Ties: {scores['ties']}")
    print("==============================")

def play_round(players, scores):
    """Play one complete round of Tic-Tac-Toe."""
    board = [" "] * 9
    current_symbol = "X"

    display_position_guide()

    while True:
        display_board(board)

        current_player = players[current_symbol]

        move = get_player_move(
            board,
            current_player,
            current_symbol
        )

        board[move] = current_symbol

        if check_winner(board, current_symbol):
            display_board(board)

            print("================================")
            print(f"Congratulations, {current_player}!")
            print(f"{current_player} wins the game!")
            print("================================")

            scores[current_symbol] += 1
            break

        elif check_tie(board):
            display_board(board)

            print("==============================")
            print("The game ended in a tie!")
            print("==============================")

            scores["ties"] += 1
            break

        else:
            if current_symbol == "X":
                current_symbol = "O"
            else:
                current_symbol = "X"


def ask_to_play_again():
    """Ask the players whether they want to play another round."""
    while True:
        answer = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def main():
    """Run the Tic-Tac-Toe program."""
    print("================================")
    print("        TIC-TAC-TOE")
    print("================================")
    print("Welcome to Tic-Tac-Toe!")
    print("Get three symbols in a row to win.")
    print()

    player_one = get_player_name(1)
    player_two = get_player_name(2)

    players = {
        "X": player_one,
        "O": player_two,
    }

    scores = {
        "X": 0,
        "O": 0,
        "ties": 0,
    }

    print("\nPlayers:")
    print(f"{player_one} = X")
    print(f"{player_two} = O")

    game_running = True

    while game_running:
        play_round(players, scores)

        display_scores(players, scores)

        game_running = ask_to_play_again()

    print("\n================================")
    print("        FINAL RESULTS")
    print("================================")

    display_scores(players, scores)

    if scores["X"] > scores["O"]:
        print(f"\nOverall winner: {players['X']}!")

    elif scores["O"] > scores["X"]:
        print(f"\nOverall winner: {players['O']}!")

    else:
        print("\nThe overall match ended in a tie!")

    print("\nThanks for playing Tic-Tac-Toe!")


main()
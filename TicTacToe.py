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
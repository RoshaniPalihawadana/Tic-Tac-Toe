import numpy as np
import random
import time

# Creating an empty Tic-Tac-Toe board
def empty_board():
    board = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    return board

# Check for empty places on the Tic-Tac-Toe board
def empty_places(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Select random place for the player on Tic-Tac-Toe
def random_place(board, player):
    select = empty_places(board)
    current_location = random.choice(select)
    board[current_location] = player
    return board

# Check the horizontal rows for a winner
def row_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

# Check the vertical rows for a winner
def col_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                break
        if win:
            return True
    return False

# Check the diagonal rows for a winner
def diag_winner(board, player):
    # Check the primary diagonal
    win = True
    for i in range(len(board)):
        if board[i, i] != player:
            win = False
            break
    if win:
        return True

    # Check the secondary diagonal
    win = True
    for i in range(len(board)):
        if board[i, len(board) - 1 - i] != player:
            win = False
            break
    return win

# Evaluates whether there is a winner or a tie
def evaluate_game(board):
    # Winner [0 = indecisive; 1 = Player 1; 2 = Player 2; -1 = Tie]
    winner = 0
    for player in [1, 2]:
        if (row_winner(board, player) or
            col_winner(board, player) or
            diag_winner(board, player)):
            winner = player
            break  # Exit loop if we have a winner

    if np.all(board != 0) and winner == 0:
        winner = -1  # Tie
    return winner

# The main game function
def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    print("Initial Board:\n", board)
    time.sleep(1)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after move {counter} by player {player}:\n{board}")
            time.sleep(1)
            counter += 1
            winner = evaluate_game(board)
            
            if winner != 0:
                break

    return winner

# Call the tic_tac_toe function and print the winner
print("Winner is player:", tic_tac_toe())

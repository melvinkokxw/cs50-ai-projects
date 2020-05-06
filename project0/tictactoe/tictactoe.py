"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_sum = 0
    o_sum = 0

    # Find total number of X's and O's marked
    for row in board:
        x_sum += row.count(X)
        o_sum += row.count(O)

    # If number of X and O equal, X's turn. Else, O's turn
    if (x_sum == o_sum):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # For each empty spot, add corresponding possible action
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Make deep copy of board
    new_board = deepcopy(board)

    # If chosen spot is already taken, raise error
    if new_board[action[0]][action[1]] is not EMPTY:
        raise AttributeError("invalid move")

    # Else find whose turn it is and mark the board
    else:
        new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if len(set(col)) == 1 and col[0] is not EMPTY:
            return col[0]

    # Check diagonal
    if (board[1][1] is not EMPTY and
        ((board[0][0] == board[1][1] and board[2][2] == board[1][1]) or
            (board[0][2] == board[1][1] and board[2][0] == board[1][1]))):
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If there is a winner or no more possible actions
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If board is terminal board, return None
    if terminal(board):
        return None

    next_player = player(board)
    optimal_action = ()

    if next_player is X:
        value = -2
    elif next_player is O:
        value = 2

    # For each possible action from state, call function to get expected value of utility
    for action in actions(board):
        temp = expected_utility(result(board, action))
        if next_player is X and temp > value:
            value = temp
            optimal_action = action
        elif next_player is O and temp < value:
            value = temp
            optimal_action = action

    # Return action that gives highest utility
    return optimal_action


def expected_utility(board):

    # If terminal board, return utility
    if terminal(board):
        return utility(board)

    # Determine next player to make move
    next_player = player(board)
    values = []

    # Find expected_utility of child nodes
    for action in actions(board):
        values.append(expected_utility(result(board, action)))

    # If next player is X, choose highest expected_utility and return it
    if next_player is X:
        return max(values)

    # If next player is O, choose lower expected_utility and return it
    elif next_player is O:
        return min(values)

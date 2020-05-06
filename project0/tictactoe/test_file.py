import pytest

import tictactoe

X = "X"
O = "O"
EMPTY = None

emptyboard = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]

board1 = [[EMPTY, EMPTY, EMPTY],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

board2 = [[EMPTY, EMPTY, O],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

board3 = [[EMPTY, EMPTY, O],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, X]]

board4 = [[O, EMPTY, O],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, X]]

board5 = [[O, X, O],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, X]]

board6 = [[EMPTY, EMPTY, O],
          [EMPTY, X, O],
          [X, EMPTY, X]]

board7 = [[O, X, O],
          [EMPTY, X, O],
          [X, EMPTY, X]]

terminalboard1 = [[X, X, X],
                  [EMPTY, O, EMPTY],
                  [EMPTY, EMPTY, O]]

terminalboard2 = [[O, O, O],
                  [EMPTY, X, EMPTY],
                  [X, EMPTY, X]]

terminalboard3 = [[X, EMPTY, O],
                  [X, O, EMPTY],
                  [X, EMPTY, EMPTY]]

terminalboard4 = [[O, X, X],
                  [EMPTY, O, EMPTY],
                  [X, EMPTY, O]]

terminalboard5 = [[X, O, X],
                  [X, O, O],
                  [O, X, X]]


@pytest.mark.parametrize("board,player", [(emptyboard, X), (board1, O), (board2, X), (board3, O), (board4, X), (board5, O)])
def test_player(board, player):
    assert tictactoe.player(board) == player


@pytest.mark.parametrize("board,actions", [(board4, {(0, 1), (1, 0), (1, 2), (2, 0), (2, 1)}), (board5, {(1, 0), (1, 2), (2, 0), (2, 1)}), (terminalboard5, set())])
def test_actions(board, actions):
    assert tictactoe.actions(board) == actions


@pytest.mark.parametrize("board, action, result", [(emptyboard, (1, 1), board1), (board1, (0, 2), board2), (board2, (2, 2), board3)])
def test_result(board, action, result):
    assert tictactoe.result(board, action) == result


@pytest.mark.parametrize("board, winner", [(emptyboard, None), (board1, None), (terminalboard1, X), (terminalboard2, O), (terminalboard3, X), (terminalboard4, O), (terminalboard5, None)])
def test_winner(board, winner):
    assert tictactoe.winner(board) == winner


@pytest.mark.parametrize("board, terminal", [(emptyboard, False), (board1, False), (board2, False), (terminalboard2, True), (terminalboard3, True), (terminalboard4, True), (terminalboard5, True)])
def test_terminal(board, terminal):
    assert tictactoe.terminal(board) == terminal


@pytest.mark.parametrize("board, utility", [(terminalboard1, 1), (terminalboard2, -1), (terminalboard3, 1), (terminalboard4, -1), (terminalboard5, 0)])
def test_utility(board, utility):
    assert tictactoe.utility(board) == utility


@pytest.mark.parametrize("board, expected_utility", [(emptyboard, 0), (board6, 1), (board7, 0), (terminalboard1, 1), (terminalboard2, -1), (terminalboard3, 1), (terminalboard4, -1), (terminalboard5, 0)])
def test_expected_utility(board, expected_utility):
    assert tictactoe.expected_utility(board) == expected_utility


@pytest.mark.parametrize("board, action", [(board6, (0, 0)), (board7, (2, 1))])
def test_minimax(board, action):
    assert tictactoe.minimax(board) == action

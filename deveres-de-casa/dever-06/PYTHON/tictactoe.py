"""
Tic Tac Toe Player
"""

import math
import copy

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

    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if action not in actions(board):
        raise Exception("Ação inválida")

    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    lines = []

    # Linhas
    lines.extend(board)

    # Colunas
    for j in range(3):
        lines.append([
            board[0][j],
            board[1][j],
            board[2][j]
        ])

    # Diagonais
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Se alguém venceu
    if winner(board) is not None:
        return True

    # Se ainda existe espaço vazio
    for row in board:
        if EMPTY in row:
            return False

    # Empate
    return True


def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value = -math.inf
        best_move = None

        for action in actions(board):
            move_value = min_value(result(board, action))

            if move_value > value:
                value = move_value
                best_move = action

        return best_move

    else:
        value = math.inf
        best_move = None

        for action in actions(board):
            move_value = max_value(result(board, action))

            if move_value < value:
                value = move_value
                best_move = action

        return best_move


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
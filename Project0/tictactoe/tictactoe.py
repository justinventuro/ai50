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
    total_X = 0
    total_O = 0
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == X:
                total_X += 1
            elif board[row][cell] == O:
                total_O +=1
    if total_X == 0 and total_O == 0:
        return X
    elif total_X > total_O:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                ans.add((row, cell))
    return ans


def result(board, action):
    #action comes out as a coordinate [#,#]
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nboard = copy.deepcopy(board)
    p = player(board)
    if action not in actions(board):
        raise NameError("Invalid Move")
    elif terminal(board):
        raise ValueError("Game over")
    else:
        (row, cell) = action
        nboard[row][cell] = p
    return nboard




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    full_board = 0
    for row in range(3):
        for cell in range(3):
            if board[row][cell] != EMPTY:
                full_board +=1
    if full_board == 9:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #X is max player and O is min player

    if board == [[EMPTY]*3]*3:
        return (0,0)

    if player(board) == X:
        v = float("-inf")
        action_select = None
        for action in actions(board):
            minValueResult = MIN_VALUE(result(board, action))
            if minValueResult > v:
                v = minValueResult
                action_select = action

    elif player(board) == O:
        v = float("inf")
        action_select = None
        for action in actions(board):
            maxValueResult = MAX_VALUE(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                action_select = action
    print(action_select)
    return action_select

def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))

    return v

def MIN_VALUE(board):
    if terminal(board):
       return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))

    return v

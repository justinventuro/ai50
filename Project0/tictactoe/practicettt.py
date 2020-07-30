
import tictactoe as ttt


board = ttt.initial_state()

print(board)
X = "X"
O = "O"
EMPTY = None

board = [[X, O, O],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
print(board[0])
player = ttt.player(board)

print(player)

action = ttt.actions(board)

print(action)


result = ttt.result(board, action)
board = [[O, O, O],
            [X, X, O],
            [X, X, EMPTY]]
print(board[0])
winner = ttt.winner(board)
print(winner)
print(result)






"""
Tic Tac Toe Player
"""

import math
import copy
import os

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
    x = 0
    o = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x = x + 1
            if cell == "O":
                o = o + 1

    if x == o:
        return "X"
    else:
        return "O"

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range (3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise ValueError("Not valid move")

    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Test rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]

    #Test columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != EMPTY:
            return board[0][column]

    # Test diagonal 1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    # Test diagonal 2
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None) or (actions(board) == set()):
        return True
    else:
        return False

    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == "X":
            return max_value(board)[1]
        else:
            return min_value(board)[1]

    #raise NotImplementedError


def max_value(board, level=0, act=None):
    #opt_action saves the maximal utility and the action to arrive this state

    opt_action = [-1, act]
    if terminal(board):
        opt_action[0] = utility(board)
        return opt_action

    #First check if there is a winner action.
    for action in actions(board):
        if utility(result(board,action)) == 1:
            opt_action[0] = 1
            opt_action[1] = action
            return opt_action

    #If not, minimax algorithm is applied
    new_level = level + 1
    for action in actions(board):
        if opt_action[0] < min_value(result(board,action), level = new_level, act=action)[0]:
            opt_action[0] = min_value(result(board,action), act=action)[0] / new_level
            opt_action[1] = action

    return opt_action


def min_value(board, level=0, act=None):
    #opt_action saves the maximal utility and the action to arrive this state

    opt_action = [1, act]
    if terminal(board):
        opt_action[0] = utility(board)
        return opt_action

    #First check if there is a winner action.
    for action in actions(board):
        if utility(result(board,action)) == -1:
            opt_action[0] = -1
            opt_action[1] = action
            return opt_action

    #If not, minimax algorithm is applied
    new_level = level + 1
    for action in actions(board):
        if opt_action[0] > max_value(result(board,action), level = new_level, act=action)[0]:
            opt_action[0] = max_value(result(board,action),act=action)[0] / new_level
            opt_action[1] = action

    return opt_action

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(f"{i}|", end='')
        for j in range(3):
            if board[i][j] != None:
                print(f"{board[i][j]}|", end='')
            else:
                print(" |", end='')
        print("\n  _ _ _")

def main():
    board = initial_state()
    while True:
        jug = input("Which player? X or O: ")
        if jug == "X":
            ia = "O"
            break
        elif jug == "O":
            ia = "X"
            break

    while not terminal(board):
        os.system('clear')
        print_board(board)

        if player(board) == jug:
            try:
                i = int(input("Row: "))
                j = int(input("Column: "))
                if (i,j) in actions(board):
                    board = result(board,(i,j))
                else:
                    raise ValueError
            except ValueError:
                pass

        else:
            print("COM is playing")
            board = result(board, minimax(board))

    os.system('clear')
    print_board(board)
    if winner(board) == jug:
        print("You Win")
    elif winner(board):
        print("You Lose")
    else:
        print("It is a tie")

if __name__ == "__main__":
    main()
from pytest import raises
import tictactoe as ttt


#Test player function
def test_player1():
    board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]
    assert ttt.player(board) == "X"

def test_player2():
    board = [["X", "", ""],
            ["", "", ""],
            ["", "", ""]]
    assert ttt.player(board) == "O"

def test_player3():
        board = [["X", "", "O"],
                ["", "O", ""],
                ["X", "O", "X"]]
        assert ttt.player(board) == "X"

# Test actions
def test_actions1():
        board = ttt.initial_state()
        assert ttt.actions(board).difference({(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)}) == set()

def test_actions2():
        board = [["O", "X", "O"],
                 ["O", "O", "X"],
                 ["X", "O", "X"]]
        assert ttt.actions(board) == set()

def test_actions3():
        board = [[None, None, "O"],
                 ["O", None, "X"],
                 ["X", "O", None]]
        assert ttt.actions(board).difference({(0,0),(0,1),(1,1),(2,2)}) == set()

# Test results
def test_results1():
        board = [["X", None, "O"],
                 ["O", None, "X"],
                 ["X", "O", None]]
        assert ttt.result(board,(0,1)) == [["X", "X", "O"],
                                          ["O", None, "X"],
                                          ["X", "O", None]]
def test_results2():
        board = [["X", None, "O"],
                 ["O", None, "X"],
                 ["X", "O", None]]
        with raises(ValueError):
                ttt.result(board,(0,0))

#Test winner
def test_winner1_horizonal():
        board = [["X", "X", "X"],
                 ["O", "O", None],
                 [None, None, None]]
        assert ttt.winner(board) == "X"

def test_winner2_vertical():
        board = [["O", "X", "X"],
                 ["O", "X", "X"],
                 ["O", None, None]]
        assert ttt.winner(board) == "O"

def test_winner3_diag1():
        board = [["X", "O", None],
                 ["O", "X", None],
                 [None, None, "X"]]
        assert ttt.winner(board) == "X"

def test_winner4_diag2():
        board = [["X", "X", "O"],
                 ["X", "O", "X"],
                 ["O", None, None]]
        assert ttt.winner(board) == "O"

def test_winner5_none1():
        board = ttt.initial_state()
        assert ttt.winner(board) == None

def test_winner6_none2():
        board = [["X", "O", "X"],
                 ["O", "X", "X"],
                 ["O", "X", "O"]]
        assert ttt.winner(board) == None

def test_winner7_none3():
        board = [["X", "O", "X"],
                 ["O", "O", "X"],
                 ["X", None, None]]
        assert ttt.winner(board) == None

def test_terminal1():
        board = [["X", "X", "O"],
                 ["X", "O", "X"],
                 ["O", None, None]]
        assert ttt.terminal(board)

def test_terminal2():
        board = [["X", "O", "X"],
                 ["O", "X", "X"],
                 ["O", "X", "O"]]
        assert ttt.terminal(board)

def test_terminal3():
        board = [["X", "O", "O"],
                 ["O", "X", "X"],
                 ["X", None, None]]
        assert not(ttt.terminal(board))

#Test Utility
def test_utilityX():
        board = [["X", "X", "X"],
                 ["O", "O", None],
                 [None, None, None]]
        assert ttt.utility(board) == 1

def test_utilityO():
        board = [["X", "X", "O"],
                 ["X", "O", "X"],
                 ["O", None, None]]
        assert ttt.utility(board) == -1

def test_utility0():
        board = [["X", "O", "X"],
                 ["O", "X", "X"],
                 ["O", "X", "O"]]
        assert ttt.utility(board) == 0

def test_minimax1():
    board = [["X", None, "O"],
            ["X", None, "X"],
            ["O", "X", "O"]]
    assert ttt.minimax(board) == (1,1)

def test_minimax2():
    board = [["O", None, "X"],
            ["O", None, None],
            ["X", None, None]]
    assert ttt.minimax(board) == (1,1)

def test_minimax3():
    board = [["X", None, "X"],
            [None, "O", None],
            [None, None, None]]
    assert ttt.minimax(board) == (0,1)

def test_minimax4():
        board = [["X", None, None],
                [None, "O", None],
                [None, None, "X"]]
        assert (ttt.minimax(board) != (0,2)) and (ttt.minimax(board) != (2,0))

def test_minimax5():
        board = [["X", None, None],
                [None, "O", "O"],
                [None, None, "X"]]
        assert ttt.minimax(board) == (1,0)

def test_minimax6():
        board = [["X", "O", None],
                ["O", "X", "X"],
                [None, "O", "X"]]
        assert ttt.minimax(board) == None

#def test_minimax7():
 #       board = ttt.initial_state()
  #      assert ttt.minimax(board) == (0,1)

def test_minimax8():
        board = [["X", None, "X"],
                [None, "O", None],
                ["X", None, "O"]]
        assert ttt.minimax(board) in ttt.actions(board)
import numpy as np

def row_col_diag(arr):
    """
    Return 8x3 list giving the rows, columns, diagonal, and
    antidiagonal of a 3x3 matrix.
    """
    three_sets = np.zeros((8,3), dtype=int)
    for i in range(arr.shape[0]):
        three_sets[i] = arr[i]
    for i in range(arr.shape[1]):
        three_sets[i+3] = arr[:,i]
    three_sets[6] = np.diag(arr)
    three_sets[7] = np.diag(np.flipud(arr))
    return three_sets

def xo_convert(n):
    """Turn 1, -1, and 0 into, respectively, 'X', 'O', and ' '."""
    if n == 1:
        return "X"
    elif n == -1:
        return "O"
    else:
        return " "

def win(arr):
    """Return 1 or -1 if a player has won, 0 otherwise."""
    for s in np.sum(row_col_diag(arr), axis=1):
        if s in [-3,3]:
            return s // 3
    return 0

def draw(arr):
    """Return whether or not the game is drawn."""
    return int((np.count_nonzero(arr) == 9) and (not win(arr)))

def term(arr):
    """Return whether or not the game is in a terminal state."""
    return win(arr) or draw(arr)


class Board(object):
    """Board object taking a 3x3 np.array as an attribute."""
    def __init__(self):
        self.arr = np.zeros((3,3), dtype=int)

    def move(self, coord, mark):
        """
        Given a coordinate and member of {'X', 'O'}, change the board
        to reflect that move.
        """
        self.arr[coord] = mark

    def win(self):
        return win(self.arr)

    def draw(self):
        return draw(self.arr)

    def term(self):
        return term(self.arr)

    def show(self):
        """Print the current board with X's and O's."""
        m = [xo_convert(int(x)) for x in np.nditer(self.arr)]
        print("{} | {} | {}".format(*m[:3]))
        print("--+---+--")
        print("{} | {} | {}".format(*m[3:6]))
        print("--+---+--")
        print("{} | {} | {}".format(*m[6:]))
        print()

    def print_result(self):
        w = self.win()
        if w == 1:
            print("X wins!")
        elif w == -1:
            print("O wins!")
        elif self.draw():
            print("Draw!")
        else:
            print("Game is still in progress!")

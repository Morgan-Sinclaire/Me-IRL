import numpy as np

def row_col_diag(arr):
    """
    Return 8x3 list giving the rows, columns, diagonal, and
    antidiagonal of a 3x3 matrix.
    """
    three_sets = [arr[i] for i in range(arr.shape[0])]
    three_sets += [arr[:,i] for i in range(arr.shape[1])]
    three_sets.append(np.diag(arr))
    three_sets.append(np.diag(np.flipud(arr)))
    return three_sets

def xo_convert(n):
    """Turn 1, -1, and 0 into, respectively, 'X', 'O', and ' '."""
    if n == 1:
        return "X"
    elif n == -1:
        return "O"
    else:
        return " "

class Board(object):
    """Board object taking a 3x3 np.array as an attribute."""
    def __init__(self):
        self.arr = np.zeros((3,3), dtype=int)

    def check(self):
        """Return 1 or -1 if a player has won, 0 otherwise."""
        rcd_sums = [np.sum(x) for x in row_col_diag(self.arr)]
        for s in rcd_sums:
            if s in [-3,3]:
                return s
        return 0

    def move(self, coord, mark):
        """
        Given a coordinate and member of {'X', 'O'}, change the board
        to reflect that move.
        """
        if self.arr[coord]:
            print("That spot's taken!")
        else:
            self.arr[coord] = mark

    def show(self):
        """Print the current board with X's and O's."""
        m = [xo_convert(int(x)) for x in np.nditer(self.arr)]
        print("{} | {} | {}".format(*m[:3]))
        print("--+---+--")
        print("{} | {} | {}".format(*m[3:6]))
        print("--+---+--")
        print("{} | {} | {}".format(*m[6:]))
        print()

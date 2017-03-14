import numpy as np

def row_col_diag(arr):
    three_sets = [arr[i] for i in range(arr.shape[0])]
    three_sets += [arr[:,i] for i in range(arr.shape[1])]
    three_sets.append(np.diag(arr))
    three_sets.append(np.diag(np.flipud(arr)))
    return three_sets

def xo_convert(n):
    if n == 1:
        return "X"
    elif n == -1:
        return "O"
    else:
        return " "

class Board(object):
    def __init__(self):
        self.arr = np.zeros((3,3), dtype=int)

    def check(self):
        rcd_sums = [np.sum(x) for x in row_col_diag(self.arr)]
        for s in rcd_sums:
            if s in [-3,3]:
                return s
        return 0

    def move(self, coord, mark):
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

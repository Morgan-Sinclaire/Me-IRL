import numpy as np
from strats import *

def row_col_diag(arr):
    sums = [arr[i] for i in range(arr.shape[0])]
    sums += [arr[:,i] for i in range(arr.shape[1])]
    sums.append(np.diag(arr))
    sums.append(np.diag(np.flipud(arr)))
    return sums

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


def initialize():
    """Begin a game, initializing the board and 2 players."""
    print('Who is player 1?')
    p1 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    print('Who is player 2?')
    p2 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    return Board(),p1,p2

def ply(b, player, turn_num, p_num=1):
    """Play out one turn, showing the board and taking input from the player."""
    b.show()
    if player == "h":
        coord = human_play(b.arr)
    elif player == "r":
        coord = random_play(b.arr)
    elif player == "1":
        coord = one_lookahead(b.arr)

    b.move(coord, p_num)

def print_result(w):
    if w == 3:
        print("X wins!")
    elif w == -3:
        print("O wins!")
    else:
        print("Draw!")

def game():
    """Play a game of tic-tac-toe."""
    b,p1,p2 = initialize()

    turn_num = 1
    while turn_num <= 9:
        if turn_num % 2:
            ply(b, p1, turn_num, 1)
        else:
            ply(b, p2, turn_num, -1)

        w = b.check()
        if w:
            break

        turn_num += 1

    print_result(w)

game()

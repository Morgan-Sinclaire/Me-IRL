import numpy as np
import random
import ttt

def human_play(arr):
    """Query the human for a coordinate to move, and return this tuple."""
    coord = input("Where do you want to move: ").replace(",", " ").split()
    coord = tuple(map(int, coord))
    return coord

def random_play(arr):
    """Randomly pick an empty spot on the board."""
    return tuple(random.choice(list(zip(*np.where(arr == 0)))))

def first(arr):
    """Pick the first empty spot, from top-left to bottom-right."""
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i,j] == 0:
                return i,j

def place(rcd_ind, ind):
    """
    Given a number 0-7 indicating whether the coordinate is in a row,
    column, or diagonal, and an index 0-2 on that 3_set, return the
    coordinate represented.
    """
    if rcd_ind in [0, 1, 2]:
        return rcd_ind,ind
    if rcd_ind in [3, 4, 5]:
        return ind,rcd_ind-3
    if rcd_ind == 6:
        return ind,ind
    if rcd_ind == 7:
        return 2-ind,ind

def one_lookahead(arr, p=-1):
    """
    If one already has 2 in a row, play winning move.
    If opponent already has 2 in a row, play blocking move.
    Otherwise, play randomly. Play depends on which player is positive.
    """
    rcd = ttt.row_col_diag(arr)
    for i in range(len(rcd)):
        if (rcd[i] == p).sum() == 2 and not (rcd[i] == -p).sum():
            return place(i, np.where(rcd[i] == 0)[0][0])
    for i in range(len(rcd)):
        if (rcd[i] == -p).sum() == 2 and not (rcd[i] == p).sum():
            return place(i, np.where(rcd[i] == 0)[0][0])
    return random_play(arr)

def negamax(arr, p=-1):
    """
    Given a game board and a player in {1,-1}, return 1,0,-1, depending
    whether they're in a winning, drawing, or losing position under minimax.
    """
    b = Board()
    b.arr = arr
    if b.term():
        return b.win()*p,()
        # when p=-1, we want to indicate a win as 1

    m = -2

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if b.arr[i,j] == 0:
                b.arr[i,j] = p
                v,ind = negamax(arr, -p)
                v = -v
                if v > m:
                    m = v
                    mi = i
                    mj = j
                b.arr[i,j] = 0

    return m,(mi,mj)

def minimax(arr, p=-1):
    return negamax(arr, p)[1]

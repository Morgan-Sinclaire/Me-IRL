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

def one_lookahead(arr, pos=1):
    """
    If one already has 2 in a row, play winning move.
    If opponent already has 2 in a row, play blocking move.
    Otherwise, play randomly. Play depends on which player is positive.
    """
    rcd = ttt.row_col_diag(arr)
    for i in range(len(rcd)):
        if (rcd[i] == pos).sum() == 2 and not (rcd[i] == -pos).sum():
            return place(i, np.where(rcd[i] == 0)[0][0])
    for i in range(len(rcd)):
        if (rcd[i] == -pos).sum() == 2 and not (rcd[i] == pos).sum():
            return place(i, np.where(rcd[i] == 0)[0][0])
    return random_play(arr)

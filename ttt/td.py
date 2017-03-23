import numpy as np
import itertools
from collections import Counter
import ttt

# for all possible board positions, value wins as 1, losses as -1,
# and all else as 0
d = {}
for p in itertools.product((-1,0,1), repeat=9):
    c = Counter(p)
    if c[1] - c[-1] in (0,1):
        t = tuple(p[i:i+3] for i in (0,3,6))
        d[t] = ttt.win(np.array(t))

# initialize explore/exploit proportion and learning rate
explore = .5
lr = .1

import run
import itertools

strats = ('r', '1')

for players in itertools.product(strats, repeat=2):
    x = 0
    o = 0
    d = 0

    for i in range(1000):
        w = run.game(players=players)
        if w == 1:
            x += 1
        elif w:
            o += 1
        else:
            d += 1

    print(players)
    print("X: {}".format(x))
    print("O: {}".format(o))
    print("D: {}".format(d))

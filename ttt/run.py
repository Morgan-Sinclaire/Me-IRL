import ttt
import strats

def initialize():
    """Begin a game, initializing the board and 2 players."""
    print('Who is player 1?')
    p1 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    print('Who is player 2?')
    p2 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    return ttt.Board(),p1,p2

def ply(b, player, turn_num, p_num, verbose):
    """Play out one turn, showing the board and taking input from the player."""
    if verbose:
        b.show()
    if player == "h":
        coord = strats.human_play(b.arr)
    elif player == "r":
        coord = strats.random_play(b.arr)
    elif player == "1":
        coord = strats.one_lookahead(b.arr, p_num)

    b.move(coord, p_num)

def game(players=False):
    """Play a game of tic-tac-toe."""
    if players:
        verbose=False
        b = ttt.Board()
        p1,p2 = players
    else:
        verbose=True
        b,p1,p2 = initialize()

    turn_num = 1
    while not b.term:
        if turn_num % 2:
            ply(b, p1, turn_num, 1, verbose)
        else:
            ply(b, p2, turn_num, -1, verbose)

        turn_num += 1

    if verbose:
        b.print_result()
    else:
        return b.win()

if __name__ == '__main__':
    game()

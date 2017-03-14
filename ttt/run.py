import ttt
import strats

def initialize():
    """Begin a game, initializing the board and 2 players."""
    print('Who is player 1?')
    p1 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    print('Who is player 2?')
    p2 = input('h for human, r for random AI, 1 for 1-move lookahead:')
    return ttt.Board(),p1,p2

def ply(b, player, turn_num, p_num):
    """Play out one turn, showing the board and taking input from the player."""
    b.show()
    if player == "h":
        coord = strats.human_play(b.arr)
    elif player == "r":
        coord = strats.random_play(b.arr)
    elif player == "1":
        coord = strats.one_lookahead(b.arr, p_num)

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

from tictactoe import TicTacToe


def main():
    tic_tac_toe = TicTacToe()

    while not tic_tac_toe.game_over:
        player_input = input('Type your next move: ')
        moves = player_input.split()
        x = int(moves[0])
        y = int(moves[1])

        tic_tac_toe.play(x, y)

if __name__ == '__main__':
    main()

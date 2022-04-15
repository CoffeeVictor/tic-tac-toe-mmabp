from typing import List, Union


def check_repeating_elements(lists: List[List[str]]):
    for current_list in lists:
        is_filled = current_list[0] != ' '
        all_elements_equal = len(set(current_list)) == 1

        if is_filled and all_elements_equal:
            return current_list[0]
    return None

def check_rows(board: List[List[str]]):
        return check_repeating_elements(board)

def check_columns(board: List[List[str]]):
    size = len(board)

    columns = [
        [
            board[row][col] for row in range(size)
        ] for col in range(size)
    ]

    return check_repeating_elements(columns)

def check_diagonals(board: List[List[str]]):
    size = len(board)

    diagonals = [
        [board[index][index] for index in range(size)],
        [board[index][size - index - 1] for index in range(size)]
    ]

    return check_repeating_elements(diagonals)

class TicTacToe:

    def __init__(self, scale = 3) -> None:
        self.scale = scale
        self.current_player = 'X'
        self.board = [
            [' ' for _ in range(scale)] for _ in range(scale)
        ]
        self.game_over = False
        self.show_board()
        print(self.current_player + ' turn!')

    def show_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def check_tie(self):
        for row in self.board:
            for spot in row:
                if spot != ' ':
                    return False
        return True

    def check_winner(self):
        return check_rows(self.board) or check_diagonals(self.board) or check_columns(self.board)

    def next_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        print(self.current_player + ' turn!')
    
    def play(self, x: int, y: int) -> Union[str, None]:

        if self.game_over:
            return

        if self.board[y][x] != ' ':
            print('Invalid move')
            return

        self.board[y][x] = self.current_player

        self.show_board()

        winner = self.check_winner()

        if winner:
            print('Winner is', winner)
            self.game_over = True
            return

        if self.check_tie():
            print('Tie!')
            self.game_over = True
            return

        self.next_player()




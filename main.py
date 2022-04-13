from typing import List

board = [
    ['a', 'x', 'a'],
    ['a', 'a', 'x'],
    ['x', 'x', 'a'],
]

test_board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def pprint(matrix: List[List[str]]):
    for row in matrix:
        print(' '.join(row))
    print()

def check_repeating_elements(lists: List[List[str]]):
    for current_list in lists:
        is_filled = current_list[0] != ''
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

def check_winner(board: List[List[str]] = None):
    return check_rows(board) or check_diagonals(board) or check_columns(board)

print(check_winner(board))

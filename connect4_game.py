from termcolor import colored

ROW_COUNT = 6
COLUMN_COUNT = 7

# NO_PIECE = u'\u25A1'
NO_PIECE = colored('X', color = 'red')
PIECE_ONE = u'\U0001F534'
PIECE_TWO = u'\U0001F535'

board = []

def new_board(board):
    for dummy in range(ROW_COUNT):
        board.append([NO_PIECE]*COLUMN_COUNT)
    return board


def print_board(board):
    for row in reversed(board):
        print(row)


def is_location_valid_for_turn(board, col):
    return board[ROW_COUNT-1][col] == NO_PIECE


def make_turn(board, row, col, piece):
    board[row][col] = piece


def get_next_free_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == NO_PIECE:
            return r


board = new_board(board)
print_board(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1 making turn(0-6): '))

        if is_location_valid_for_turn(board, col):
            row = get_next_free_row(board, col)
            make_turn(board, row, col, PIECE_ONE)
    
    else:
        col = int(input('Player 2 making turn(0-6): '))

        if is_location_valid_for_turn(board, col):
            row = get_next_free_row(board, col)
            make_turn(board, row, col, PIECE_TWO)
    
    turn += 1
    turn = turn % 2
    print_board(board)




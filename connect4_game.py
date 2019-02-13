from termcolor import colored

ROW_COUNT = 6
COLUMN_COUNT = 7

NO_PIECE = '[_]'
PIECE_ONE = colored('[X]', color = 'red')
PIECE_TWO = colored('[O]', color = 'blue')


board = []
def new_board(board):
    for dummy in range(ROW_COUNT):
        board.append([NO_PIECE]*COLUMN_COUNT)
    return board


def draw_board(board):
    for row in reversed(board):
        for element in range(len(row)):
            if element != len(row)-1:
                print(row[element], end = "")
            else:
                print(row[element])


def is_location_valid_for_turn(board, col):
    try:
        return board[ROW_COUNT-1][col] == NO_PIECE
    except IndexError:
        print('You must choose the number of columnt between 1 and ' + str(COLUMN_COUNT))


def make_turn(board, row, col, piece):
    board[row][col] = piece


def get_next_free_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == NO_PIECE:
            return r


board = new_board(board)
draw_board(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1 making turn(1-7): '))
        col_number = col - 1

        if is_location_valid_for_turn(board, col_number):
            row = get_next_free_row(board, col_number)
            make_turn(board, row, col_number, PIECE_ONE)
    
    else: 
        col = int(input('Player 2 making turn(1-7): '))
        col_number = col -1
        
        if is_location_valid_for_turn(board, col_number):
            row = get_next_free_row(board, col_number)
            make_turn(board, row, col_number, PIECE_TWO)
    
    turn += 1
    turn = turn % 2
    draw_board(board)
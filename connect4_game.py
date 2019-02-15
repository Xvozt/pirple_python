from termcolor import colored

"""This is the connect 4 game.
The player choosing the column on the playing board.
The player's piece is dropped from the top into grid.
The pieces fall straight down.
The piece occupying the lowest available space within the column
After that turn is passed to the next player.
The first player formed vertical, horizontal or diagonal line of pieces wins.
"""


ROW_COUNT = 6
COLUMN_COUNT = 7

NO_PIECE = '[_]'
PIECE_ONE = colored('[X]', color='red', attrs=['bold'])
PIECE_TWO = colored('[O]', color='blue', attrs=['bold'])


def new_board(board):
    """Function creates new board by making list of lists

    Arguments:
        board {list} -- empty list

    Returns:
        [list] -- list filled with NO_PIECE to create "empty" playing board
    """
    for dummy in range(ROW_COUNT):
        board.append([NO_PIECE]*COLUMN_COUNT)
    return board


def draw_board(board):
    """Function drawing playing board with individual NO_PIECE elements

    Arguments:
        board {list} -- list of lists filled with NO_PIECE elements
    """
    for row in reversed(board):
        for element in range(len(row)):
            if element != len(row)-1:
                print(row[element], end="")
            else:
                print(row[element])


def is_location_valid_for_turn(board, col):
    """Function checking if chosen spot for turn has NO_PIECE in it

    Arguments:
        board {list} -- playing board
        col {int} -- the number of chosen column for the turn

    Returns:
        boolean -- True if spot is vaild for turn, False otherwise
    """
    try:
        return board[ROW_COUNT-1][col] == NO_PIECE
    except IndexError:
        print('You must choose the number of columnt between 1 and ' +
              str(COLUMN_COUNT))


def make_move(board, row, col, piece):
    """Function is placing the piece of a player into chosen spot

    Arguments:
        board {list} -- playing board
        row {int} -- row of the playing board
        col {int} -- column of the playing board
        piece {str} -- the piece symbol, depends on the player
    """
    board[row][col] = piece


def get_next_free_row(board, col):
    """The function chosing the row with NO_PIECE element
    after player chose column for turn

    Arguments:
        board {list} -- playing board
        col {int} -- chosen column

    Returns:
        int -- the row number of the free row
    """
    for r in range(ROW_COUNT):
        if board[r][col] == NO_PIECE:
            return r


def winning_move(board, piece):
    """Function checking after the player's move was winning.
    Function scan playing board.
    If there is 4 same pieces are placed in 3 types of line.
    Types of lines: horizontal, vertical, diagonal.
    If it found 4 pieces then player who's piece is it won.
    There 4 for loops for each case.
    TODO: optimize searching for winning move

    Arguments:
        board {list} -- playing board
        piece {str} -- the piece symbol depends on the player

    Returns:
        boolean -- True if move was winning
    """
# Horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] \
                    == board[r][c+1] \
                    == board[r][c+2] \
                    == board[r][c+3] \
                    == piece:
                return True
# Vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] \
                    == board[r+1][c] \
                    == board[r+2][c] \
                    == board[r+3][c] \
                    == piece:
                return True
# Positive diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] \
                    == board[r+1][c+1] \
                    == board[r+2][c+2] \
                    == board[r+3][c+3] \
                    == piece:
                return True
# Positive diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] \
                    == board[r-1][c+1] \
                    == board[r-2][c+2] \
                    == board[r-3][c+3] \
                    == piece:
                return True


def main():
    """The function creating and drawing playing board.
    After that in while loop changing playing turns.
    For each player turn calls functions to:
    check location, get next row and check for win move.
    If someone wins printing winner message.
    """
    board = []
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
                make_move(board, row, col_number, PIECE_ONE)
                if winning_move(board, PIECE_ONE):
                    print(colored('PLAYER 1 WINS!', 'red', attrs=['bold']))
                    game_over = True

        else:
            col = int(input('Player 2 making turn(1-7): '))
            col_number = col - 1

            if is_location_valid_for_turn(board, col_number):
                row = get_next_free_row(board, col_number)
                make_move(board, row, col_number, PIECE_TWO)
                if winning_move(board, PIECE_TWO):
                    print(colored('PLAYER 2 WINS!', 'blue', attrs=['bold']))
                    game_over = True

        turn += 1
        turn = turn % 2
        draw_board(board)


main()

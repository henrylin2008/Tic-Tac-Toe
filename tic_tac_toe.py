import random

# TODO
# 1. We need to print a board.
# 2. Take in player input.
# 3. Place their input on the board.
# 4. Check if the game is won,tied, lost, or ongoing.
# 5. Repeat c and d until the game has been won or tied.
# 6. Ask if players want to play again.

# 1. Display board
# 2. Accepting User Input
# 3. Validate input: input is digit type, and value is between 1 and 10
# 4.

game_list = [0, 1, 2]
game_on = True
test_board = ['#', 'x', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


# test_board = [' ']*10


def clear_board():
    print('\n' * 100)


def display_board(board):
    clear_board()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])


def player_input():
    """Players pick his/her mark
    Output = (Player 1 marker, Player 2 marker)
    """

    marker = ''

    # keep asking player 1 to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, '$', 2)
# display_board(test_board)


def win_check(board, mark):
    # Win Tic-Tac-Toe?
    # All rows: share the same marker
    # All columns: check if marker matches
    # 2 diagonals, check to see match
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# display_board(test_board)
# win_check(test_board, 'X')


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# choose_first()


def space_check(board, position):
    # determine if a space on the board is freely available
    return board[position] == ' '


def full_board_check(board):
    # Check if the board is full, True if Full, False otherwise
    for i in range(1, 10):
        if space_check(board, i):  # if there's available space, return False
            return False
    # Board is Full if return True
    return True


def player_choice(board):
    """
    Asks for player's next position; Check if it's a free position, if it is, return the position for later use
    """
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))

    return position


def replay():
    """

    """
    choice = input("Play again? Enter Yes or No ").lower()

    return choice == 'yes'

# replay()

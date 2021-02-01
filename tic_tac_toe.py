import random

# TODO
# 1. We need to print a board.
# 2. Take in player input.
# 3. Place their input on the board.
# 4. Check if the game is won,tied, lost, or ongoing.
# 5. Repeat c and d until the game has been won or tied.
# 6. Ask if players want to play again.

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
        print("Please select a valid space")

    return position


def replay():
    """

    """
    choice = input("Play again? Enter Yes or No ").lower()

    return choice == 'yes' or choice == 'y'

# replay()


# While loop to keep running the game
print("Tic Tac Toe")

while True:

    # Play the game

    # set up: Board, who's first, choose Markers X, O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play? y or n? ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game Play
    while game_on:
        if turn == 'Player 1':

            #show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has Won!")
                game_on = False    # game over
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    # next player's turn
                    turn = 'Player 2'

        else:
            #show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has Won!")
                game_on = False    # game over
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    # next player's turn
                    turn = 'Player 1'

    if not replay():
        break
# break out of the while loop on replay()

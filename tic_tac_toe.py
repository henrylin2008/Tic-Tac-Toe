import os
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
# test_board = ['#', 'x', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
test_board = [' ']*10


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
    """Players pick his/her mark"""
    marker = ''

    # keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2



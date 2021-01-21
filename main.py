import random


# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('_____')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('_____')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    sign = ''
    while not (sign == 'X' or sign == 'O'):
        sign = input("Player 1, Do you want to be X or O?").upper()
    if sign == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_sign(board, position, sign):
    board[position] = sign


def check_win(board, sign):
    return ((board[7] == sign and board[8] == sign and board[9] == sign) or
            (board[4] == sign and board[5] == sign and board[6] == sign) or
            (board[1] == sign and board[2] == sign and board[3] == sign) or
            (board[7] == sign and board[4] == sign and board[1] == sign) or
            (board[8] == sign and board[5] == sign and board[2] == sign) or
            (board[9] == sign and board[6] == sign and board[3] == sign) or
            (board[1] == sign and board[5] == sign and board[9] == sign) or
            (board[7] == sign and board[5] == sign and board[3] == sign))


# Randomly decide which player goes first
def randomly_choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def is_position_empty(board, position):
    return board[position] == ' '


def is_board_full(board):
    for i in range(1, 10):
        if is_position_empty(board, i):
            return False
    return True


# Function to take player's next choice for placing the sign
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_position_empty(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    is_replay = input("Do you want to play again? Enter Y or N: ")
    if is_replay.lower().startswith('y'):
        return True
    else:
        return False


def game():
    print("Welcome to the Tic-Tac-Toe game!")
    while True:
        board = [' '] * 10
        player1_sign, player2_sign = player_input()
        turn = randomly_choose_first()
        print(turn + " will play first")

        start_game = input("Do you want to start playing? Enter Y or N")

        if start_game.lower() == 'y':
            is_game = True
        else:
            is_game = False

        while is_game:
            if turn == 'Player 1':
                display(board)
                position = player_choice(board)

                place_sign(board, position, player1_sign)

                if check_win(board, player1_sign):
                    display(board)
                    print("Congratulations!! You Player 1  won the game!")
                    is_game = False
                else:
                    if is_board_full(board):
                        display(board)
                        print("It's a draw!")
                        break
                    else:
                        turn = 'Player 2'

            else:
                display(board)
                position = player_choice(board)
                place_sign(board, position, player2_sign)

                if check_win(board, player2_sign):
                    display(board)
                    print("Congratulations!! Player 2  won the game!")
                    is_game = False
                else:
                    if is_board_full(board):
                        display(board)
                        print("It's a draw!")
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break


# print(player_input())
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display(test_board)
# place_sign(board, 8, '%')
# print(check_win(test_board, 'X'))


# display(board)
game()

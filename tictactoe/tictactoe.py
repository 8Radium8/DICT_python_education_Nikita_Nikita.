import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def check_winner(mark):
    return ((board[0] == board[1] == board[2] == mark) or
            (board[3] == board[4] == board[5] == mark) or
            (board[6] == board[7] == board[8] == mark) or
            (board[0] == board[3] == board[6] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[0] == board[4] == board[8] == mark) or
            (board[2] == board[4] == board[6] == mark))
def check_space(position):
    return board[position] == "-"
def make_move(position, mark):
    board[position] = mark
def check_tie():
    return "-" not in board
def player_choice():
    position = input("Choose position (1-9): ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Incorrect. Choose another position (1-9): ")
    return int(position) - 1
def play_game():
    print("Game started!")
    display_board()

    while True:
        position = player_choice()
        while not check_space(position):
            position = player_choice()
        make_move(position, "X")
        display_board()
        if check_winner("X"):
            print("You win!")
            break
        elif check_tie():
            print("Draw!")
            break
        position = random.randint(0, 8)
        while not check_space(position):
            position = random.randint(0, 8)
        make_move(position, "O")
        display_board()
        if check_winner("O"):
            print("Lol. Computer win!")
            break
        elif check_tie():
            print("Draw!")
            break
play_game()

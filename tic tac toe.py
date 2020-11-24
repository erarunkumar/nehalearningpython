#---------------global variable---------------
board = ["-", "-","-",
        "-","-","-",
        "-","-","-",]
game_still_going_on = True
winner = None
current_player = "x"

def display_board():
    print(board[0]+" | " +board[1]+" | "+board[2])
    print(board[3]+" | " +board[4]+" | "+board[5])
    print(board[6]+" | " +board[7]+" | "+board[8])

def play_game():

    display_board()
    while game_still_going_on:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "x" or winner == "0" :
        print(winner + "won")
    elif winner == None:
        print("tie")

def handle_turn(player):

    print(player + "'s turn")

    position =(input("choose position from 1 to 9"))
    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position= input("choose position from 1 to 9")

        position =int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("u can't go there . please ")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner

    row_winner =check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
        return
def check_rows():
    global  game_still_going_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():

    global game_still_going_on

    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"
    if columns_1 or columns_2 or columns_3:
        game_still_going_on = False

    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going_on
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going_on = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going_on
    if "-" not in board:
        game_still_going_on = False
        return

def flip_player():
    global current_player
    if current_player == "x":
        current_player = "0"
    elif current_player =="0":
        current_player = "x"

play_game()
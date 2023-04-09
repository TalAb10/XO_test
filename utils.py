import numpy as np

def print_board(board):
    num_of_tabs = 5
    print(num_of_tabs * "\t" + "    The Gaming Board ")
    print(num_of_tabs * "\t" + " _____________________ ")
    for line in board:
        print(num_of_tabs * "\t" + "|",end="")
        for value in line:
            print(value,end="")
        print("|")
    print(num_of_tabs * "\t" +" _____________________ ")

def check_if_won(board, spot_index, slot_str_format = "", player_value=""):
    won = np.all(board[spot_index[0]] == slot_str_format.format(player_value)) or\
          np.all(board[:,spot_index[1]] == slot_str_format.format(player_value)) or \
          np.all(np.diag(board) == slot_str_format.format(player_value)) or \
          np.all(np.diag(board[::-1]) == slot_str_format.format(player_value))

    return won
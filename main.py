import numpy as np
from utils import print_board,check_if_won

play_again = 1
slot_str_format = '   {}   '

while(play_again):
    print("|---------------------------New Game---------------------------|")
    board = np.array([[slot_str_format.format('1'),slot_str_format.format('2'),slot_str_format.format('3')],
                      [slot_str_format.format('4'),slot_str_format.format('5'),slot_str_format.format('6')],
                      [slot_str_format.format('7'),slot_str_format.format('8'),slot_str_format.format('9')]])

    player_won = False
    count_plays = 1
    while(not player_won):

        print_board(board)
        if(count_plays == 10):
            print("Ow, looks like we dont have a winner, but maybe next time!")
            break

        if(count_plays % 2):
            player_value = 'X'
        else:
            player_value = 'O'

        slot_int_val = int(input(f"Player {player_value}, please submit the slot's index you would like to put {player_value} in:\n")) - 1
        slot_board_indexes = [slot_int_val//3,slot_int_val%3]

        if (board[slot_board_indexes[0],slot_board_indexes[1]] != slot_str_format.format(slot_int_val+1)):
            print(f"-------------------------------------------------------------------------------------\n"
                  f"Please submit slot's index that isn't already been submitted:\n")
            continue

        board[slot_board_indexes[0],slot_board_indexes[1]] = slot_str_format.format(player_value)
        player_won = check_if_won(board, slot_board_indexes, slot_str_format,  player_value)
        count_plays += 1

        if(player_won):
            print_board(board)
            print(f"-------------------------------------------------------------------------------------\n"
              f"Player {player_value} won!\n"
              f"That was amazing!")

    play_again = bool(int(input(
        f"-------------------------------------------------------------------------------------\n"
        f"Submit 1 if you want to play again or 0, if you don't:\n")))

print("\nThat was very fun!\n"
      "Hope to see you again.")




from random import randint
from time import sleep

snakes = {
    32 : 10,
    62 : 18,
    48 : 26,
    88 : 24,
    95 : 56
}

ladders = {
    1 : 38,
    4 : 14,
    8 : 30,
    21 : 42,
    28 : 72,
    50 : 67,
    71 : 92,
    80 : 99
}

player_dict = {}


def roll_dice(no_of_dice):
    return randint(1, 6 * no_of_dice)



def check_snake_ladder(val):
    if val in snakes:
        return snakes[val]
    elif val in ladders:
        return ladders[val]
    return False


def update_pos(player_no, dice_val):
    if (player_dict[player_no] + dice_val) > 100:
        print(str(player_no)+" need {} to win".format(str(100-player_dict[player_no])))
        return

    if (player_dict[player_no] + dice_val) == 100:
        print('{} won'.format(str(player_no)))
        return True

    if player_dict[player_no] == 0 and dice_val == 6:
        player_dict[player_no] = 1

    snake_ladder_check = check_snake_ladder(player_dict[player_no]+dice_val)
    if not snake_ladder_check:
        player_dict[player_no] = player_dict[player_no] + dice_val
        return

    player_dict[player_no] = snake_ladder_check
    return



if __name__ == '__main__':

    no_of_players = input("Enter number of players: ")
    no_of_dice = input("Enter the number of dices: ")
    if no_of_players and no_of_dice:
        for i in range(1, int(no_of_players)+1):
            player_dict[i] = 0

        win_flag = False
        while True:
            print(player_dict)
            for val in player_dict:
                player_1_val = roll_dice(int(no_of_dice))
                win_status = update_pos(val, player_1_val)
                if win_status:
                    win_flag = True
                    break
                sleep(1)
            if win_flag:
                break
    else:
        print("Number of players and number of dice must be greater than zero")








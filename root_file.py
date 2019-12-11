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

player_dict = {
    1: 0,
    2 :0
}


def roll_dice():
    dice_val = randint(1, 6)
    return dice_val


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


    while True:
        print(player_dict)
        player_1_val = roll_dice()
        win_status = update_pos(1, player_1_val)
        if win_status:
            break
        sleep(1)
        player_2_val = roll_dice()
        win_status = update_pos(2, player_2_val)
        if win_status:
            break






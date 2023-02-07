import random
import time

game_field = [[3.1, 3.2, 3.3], [2.1, 2.2, 2.3], [1.1, 1.2, 1.3]]
used = []


def print_field():
    for line in game_field:
        for place in line:
            if place == 0:
                print("\033[31m{}".format(place), end="\t")
            elif place == "X":
                print("\033[34m{}".format(place), end="\t")
            else:
                print("\033[0m{}".format("□"), end="\t")
        print("\n")
    print("\033[0m".format())


def player_3_version(sign):
    while True:
        try:
            y, x = input().split()

            turn = str(str(x) + "." + str(y)).strip()
            turn = float(turn)
            while turn in used or not 0 < turn < 4:
                print("input correct number")
                y, x = input().split()
                turn = str(str(x) + "." + str(y)).strip()
                turn = float(turn)
            for i in range(len(game_field)):
                for j in range(len(game_field)):
                    if game_field[i][j] == turn:
                        used.append(game_field[i][j])
                        game_field[i][j] = sign
            break
        except ValueError:
            print("input x and y")


def bot_3_version(sign):
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    turn = str(str(x) + "." + str(y))
    turn = float(turn)
    while turn in used:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        turn = str(str(x) + "." + str(y))
        turn = float(turn)
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == turn:
                used.append(game_field[i][j])
                game_field[i][j] = sign


def game_over():
    for line in game_field:
        if line[0] == line[1] == line[2]:
            return True
    for j in range(len(game_field)):
        if game_field[0][j] == game_field[1][j] == game_field[2][j]:
            return True
    if game_field[0][0] == game_field[1][1] == game_field[2][2]:
        return True
    if game_field[0][2] == game_field[1][1] == game_field[2][0]:
        return True
    if len(used) == 9:
        return "Tie"
    return False


def game_mode():
    print("Pick game mode:\n 1)PvP\n 2)PvAI\n 3)AIvsAI")
    mode = int(input())
    while not 0 < mode < 4:
        print("INPUT CORRECT NUMBER U DUMB FUCK!")
        mode = int(input())
    if mode == 1:
        print("player #1 name?")
        player_1_name = input()
        print("player #2 name?")
        player_2_name = input()
        return mode, player_1_name, player_2_name
    elif mode == 2:
        print("player name?")
        player_name = input()
        return mode, player_name, "Bot"
    elif mode == 3:
        return mode, "Bot#1", "Bot#2"

    return mode


def game():
    def player_vs_player(p1: str, p2: str) -> str:
        # Переменные должны называтся емко и без спецсимволов(желательно)
        # ты можешь указать что выдает функция и что принимает прямо как в статических языках,
        # привыйка писать так потом будет легче читать твой код
        winner = str()
        while True:
            # player 1 turn
            print_field()
            print(p1 + " turn")
            player_3_version("X")
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = p1
                break

            # player 2 turn
            print_field()
            print(p2 + " turn")
            player_3_version(0)
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = p2
                break

            continue
        return winner

    def player_vs_bot(p: str, b: str) -> str:
        winner = str()
        while True:
            # player 1 turn
            print_field()
            print(p + " turn")
            player_3_version("X")
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = p
                break

            # player 2 turn
            print_field()
            print(b + " turn")
            bot_3_version(0)
            time.sleep(1)
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = b
                break

            continue
        return winner

    def bot_vs_bot(p1: str, p2: str) -> str:
        winner = str()
        while True:
            # player 1 turn
            print_field()
            print(p1 + " turn")
            bot_3_version("X")
            time.sleep(1)
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = p1
                break
            # player 2 turn
            print_field()
            print(p2 + " turn")
            bot_3_version(0)
            time.sleep(1)
            if game_over() == "Tie":
                winner = "Tie"
                break
            elif game_over():
                winner = p2
                break

            continue
        return winner
    win = str()
    mode, player_1_name, player_2_name = game_mode()
    if mode == 1:
        win = player_vs_player(player_1_name, player_2_name)
    elif mode == 2:
        win = player_vs_bot(player_1_name, player_2_name)
    elif mode == 3:
        win = bot_vs_bot(player_1_name, player_2_name)

    print_field()

    if win == "Tie":
        print("Tie")

    else:
        print(f"{win} WIN")


game()

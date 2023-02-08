import random
import time

while True:
    try:
        size = int(input("Input field size:\n"))
        win_size = int(input("Input size of line to win:\n"))
        while size < win_size:
            print("Field size must be more then size of line ")
            size = int(input("Input field size:\n"))
            win_size = int(input("Input size of line to win:\n"))
        break
    except ValueError or IndexError:
        print("Input correct numbers")

field = [["□"] * size for i in range(size)]


# def create_field():
#     field = [["□"] * size for i in range(size)]
#     return field


def print_field():
    for line in field:
        for place in line:
            if place == 0:
                print("\033[31m{}".format(place), end="\t")
            elif place == "X":
                print("\033[34m{}".format(place), end="\t")
            else:
                print("\033[0m{}".format("□"), end="\t")
        print("\n")
    print("\033[0m".format())


def start():
    win = str()
    mode, p1_name, p2_name = prompt()

    if mode == 1:
        win = player_vs_player(p1_name, p2_name)
    elif mode == 2:
        win = player_vs_bot(p1_name, p2_name)
    elif mode == 3:
        win = bot_vs_bot(p1_name, p2_name)

    print_field()

    if win == "Tie":
        print("Tie")

    else:
        print(f"{win} WIN")


def player_vs_player(p1: str, p2: str) -> str:
    winner = str()
    while True:
        # player 1 turn
        print_field()
        print(p1 + " turn")
        sign = "X"
        player(sign)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
            winner = p1
            break

        # player 2 turn
        print_field()
        print(p2 + " turn")
        sign = 0
        player(sign)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
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
        sign = "X"
        player(sign)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
            winner = p
            break

        # player 2 turn
        print_field()
        print(b + " turn")
        sign = 0
        bot(sign)
        time.sleep(1)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
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
        sign = "X"
        bot(sign)
        time.sleep(1)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
            winner = p1
            break

        # player 2 turn
        print_field()
        print(p2 + " turn")
        sign = 0
        bot(sign)
        time.sleep(1)
        if check_new(sign) == "Tie":
            winner = "Tie"
            break
        elif check_new(sign):
            winner = p2
            break

        continue
    return winner


def player(sign):
    while True:
        try:
            y, x = input().split()
            x = int(x) - 1
            y = int(y) - 1
            while field[x][y] != "□":
                print("Input correct numbers(X and Y)")
                y, x = input().split()
                x = int(x) - 1
                y = int(y) - 1
            field[x][y] = sign
            break
        except ValueError or IndexError:
            print("Input 2 correct numbers: x and y")


def bot(sign):
    x = random.randint(0, size - 1)
    y = random.randint(1, size - 1)
    while field[x][y] != "□":
        x = random.randint(0, size - 1)
        y = random.randint(1, size - 1)
    field[x][y] = sign


def check_new(sign):
    for line in field:
        for i in range(len(field) - (win_size - 1)):
            cnt = 0
            for j in range(i, win_size - 1 + i):
                if line[j] == line[j + 1] and line[j] == sign:
                    cnt += 1
            if cnt == win_size - 1:
                return True

    for column in range(len(field)):
        for i in range(len(field) - (win_size - 1)):
            cnt = 0
            for j in range(i, win_size - 1 + i):
                if field[j][column] == field[j + 1][column] == sign:
                    cnt += 1
            if cnt == win_size - 1:
                return True

    for i in range(len(field) - (win_size - 1)):
        for j in range(len(field) - (win_size - 1)):
            cnt = 0
            for c in range(win_size - 1):
                if field[i + c][j + c] == field[i + c + 1][j + c + 1] == sign:
                    cnt += 1
            if cnt == win_size - 1:
                return True

    for i in range(len(field) - win_size, len(field)):
        for j in range(len(field) - (win_size - 1)):
            cnt = 0
            for c in range(win_size - 1):
                if field[i - c][j + c] == field[i - c - 1][j + c + 1] == sign:
                    cnt += 1
            if cnt == win_size - 1:
                return True

    return False


def prompt():
    print("Pick game mode:\n 1)player_vs_player\n 2)player_vs_bot\n 3)bot_vs_bot")
    mode = int(input())
    while not 0 < mode < 4:
        print("Input correct number, please!!")
        mode = int(input())
    if mode == 1:
        print("player #1 name?")
        p1_name = input()
        print("player #2 name?")
        p2_name = input()
        return mode, p1_name, p2_name
    elif mode == 2:
        print("player name?")
        player_name = input()
        return mode, player_name, "Bot"
    elif mode == 3:
        return mode, "Bot#1", "Bot#2"

    return mode


start()

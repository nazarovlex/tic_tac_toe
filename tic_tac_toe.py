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


def win_print(win_line):
    for i in range(len(field)):
        for j in range(len(field)):
            if [i, j] in win_line:
                print("\033[1;33m{}".format(field[i][j]), end="\t")
            elif field[i][j] == 0:
                print("\033[31m{}".format(field[i][j]), end="\t")
            elif field[i][j] == "X":
                print("\033[34m{}".format(field[i][j]), end="\t")
            else:
                print("\033[0m{}".format("□"), end="\t")
        print("\n")
    print("\033[0m".format())


def start():
    win, win_line = str(), str()
    mode, p1_name, p2_name = prompt()

    if mode == 1:
        win, win_line = player_vs_player(p1_name, p2_name)
    elif mode == 2:
        win, win_line = player_vs_bot(p1_name, p2_name)
    elif mode == 3:
        win, win_line = bot_vs_bot(p1_name, p2_name)

    if win == "Tie":
        print("Tie")
        print_field()
    else:
        print(f"{win} WIN")
        win_print(win_line)


def player_vs_player(p1: str, p2: str) -> tuple[str, any]:
    winner = str()
    while True:
        # player 1 turn
        print_field()
        print(p1 + " turn")
        sign = "X"
        player(sign)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = p1
            break

        # player 2 turn
        print_field()
        print(p2 + " turn")
        sign = 0
        player(sign)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = p2
            break

        continue
    return winner, win_line


def player_vs_bot(p: str, b: str) -> tuple[str, any]:
    winner = str()
    while True:
        # player turn
        print_field()
        print(p + " turn")
        sign = "X"
        player(sign)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = p
            break

        # bot turn
        print_field()
        print(b + " turn")
        sign = 0
        bot(sign)
        time.sleep(1)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = b
            break

        continue
    return winner, win_line


def bot_vs_bot(b1: str, b2: str) -> tuple[str, any]:
    winner = str()
    while True:
        # bot#1 turn
        print_field()
        print(b1 + " turn")
        sign = "X"
        bot(sign)
        time.sleep(1)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = b1
            break

        # bot#2 turn
        print_field()
        print(b2 + " turn")
        sign = 0
        bot(sign)
        time.sleep(1)
        win_check, win_line = check(sign)
        if win_check == 1:
            winner = "Tie"
            break
        elif win_check == 2:
            winner = b2
            break

        continue
    return winner, win_line


def player(sign):
    while True:
        try:
            y, x = input().split()
            x = int(x) - 1
            y = int(y) - 1
            while field[size - 1 - x][y] != "□":
                print("Input correct numbers(X and Y)")
                y, x = input().split()
                x = int(x) - 1
                y = int(y) - 1
            field[size - 1 - x][y] = sign
            break
        except ValueError or IndexError:
            print("Input 2 correct numbers: x and y")


def bot(sign):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    while field[x][y] != "□":
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
    field[x][y] = sign


def check(sign):
    win_line = []
    for line in range(len(field)):
        for i in range(len(field) - (win_size - 1)):
            cnt = 0
            win_line = []
            for j in range(i, win_size - 1 + i):
                if [line, j] not in win_line:
                    win_line.append([line, j])
                if field[line][j] == field[line][j + 1] == sign:
                    cnt += 1
                    win_line.append([line, j + 1])
            if cnt == win_size - 1:
                return 2, win_line

    for column in range(len(field)):
        for i in range(len(field) - (win_size - 1)):
            cnt = 0
            win_line = []
            for j in range(i, win_size - 1 + i):
                if [j, column] not in win_line:
                    win_line.append([j, column])
                if field[j][column] == field[j + 1][column] == sign:
                    cnt += 1
                    win_line.append([j + 1, column])
            if cnt == win_size - 1:
                return 2, win_line

    for i in range(len(field) - (win_size - 1)):
        for j in range(len(field) - (win_size - 1)):
            cnt = 0
            win_line = []
            for c in range(win_size - 1):
                if [i + c, j + c] not in win_line:
                    win_line.append([i + c, j + c])
                if field[i + c][j + c] == field[i + c + 1][j + c + 1] == sign:
                    cnt += 1
                    win_line.append([i + c + 1, j + c + 1])
            if cnt == win_size - 1:
                return 2, win_line

    for i in range(len(field) - win_size, len(field)):
        for j in range(len(field) - (win_size - 1)):
            cnt = 0
            win_line = []
            for c in range(win_size - 1):
                if [i - c, j + c] not in win_line:
                    win_line.append([i - c, j + c])
                if field[i - c][j + c] == field[i - c - 1][j + c + 1] == sign and (i-c-1)>-1:
                    cnt += 1
                    win_line.append([i - c - 1, j + c + 1])
            if cnt == win_size - 1:
                return 2, win_line

    cnt = 0
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == "□":
                cnt += 1
    if cnt > 0:
        return 0, None
    elif cnt == 0:
        win_line = None
        return 1, win_line
    return 0, None


def prompt():
    while True:
        try:
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
        except ValueError or IndexError:
            print("Input correct numbers")

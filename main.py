import random
import time


game_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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


def player_turn(sign):
    turn = int(input())
    while turn in used:
        print("Input correct number")
        turn = int(input())
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == turn:
                used.append(game_field[i][j])
                game_field[i][j] = sign


def easy_bot(sign):
    turn = random.randint(1, 9)
    while turn in used:
        turn = random.randint(1, 9)
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


def game():
    while True:
        print_field()
        print("player 1")
        easy_bot("X")
        time.sleep(2)
        if game_over() == "Tie":
            winner = "Tie"
            break
        elif game_over():
            winner = "player 1"
            break


        print_field()
        print("player 2")
        easy_bot(0)
        time.sleep(2)
        if game_over() == "Tie":
            winner = "Tie"
            break
        elif game_over():
            winner = "player 2"
            break

        continue

    print_field()
    if winner == "Tie":
        print("Tie")

    else:
        print(f"{winner} WIN")




game()

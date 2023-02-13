import random
import time
import socket


class TicTacToe:
    def __init__(self, size, win_size, p1_name, p2_name):
        self.size = size
        self.win_size = win_size
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.field = []
        self.win_line = []

    def create_field(self):
        self.field = [["□"] * self.size for _ in range(self.size)]

    def print_field(self):
        field = self.field
        for line in field:
            for place in line:
                if place == "0":
                    print("\033[31m{}".format(place), end="\t")
                elif place == "X":
                    print("\033[34m{}".format(place), end="\t")
                else:
                    print("\033[0m{}".format("□"), end="\t")
            print("\n")
        print("\033[0m".format())

    def print_winner(self):
        field = self.field
        win_line = self.win_line
        for i in range(len(field)):
            for j in range(len(field)):
                if [i, j] in win_line:
                    print("\033[1;33m{}".format(field[i][j]), end="\t")
                elif field[i][j] == "0":
                    print("\033[31m{}".format(field[i][j]), end="\t")
                elif field[i][j] == "X":
                    print("\033[34m{}".format(field[i][j]), end="\t")
                else:
                    print("\033[0m{}".format("□"), end="\t")
            print("\n")
        print("\033[0m".format())

    def player_turn(self, sign: str):
        field = self.field
        size = self.size
        while True:
            try:
                y, x = input().split()
                x = int(x) - 1
                y = int(y) - 1

                while field[size - 1 - x][y] != "□" or not -1 < y < size or not -1 < x < size:
                    print("Input correct numbers(X and Y)")
                    y, x = input().split()
                    x = int(x) - 1
                    y = int(y) - 1
                field[size - 1 - x][y] = sign
                break
            except (ValueError, IndexError):
                print("Error: Input 2 correct numbers: x and y")
        return field

    def check_input(self):
        field = self.field
        size = self.size
        while True:
            try:
                y, x = input().split()
                x = int(x) - 1
                y = int(y) - 1

                while field[size - 1 - x][y] != "□" or not -1 < y < size or not -1 < x < size:
                    print("Input correct numbers(X and Y)")
                    y, x = input().split()
                    x = int(x) - 1
                    y = int(y) - 1
                break
            except (ValueError, IndexError):
                print("Error: Input 2 correct numbers: x and y")
        return x, y

    def player_online_turn(self, sign: str, x: int, y: int):
        field = self.field
        size = self.size
        field[size - 1 - x][y] = sign
        return field

    def bot_turn(self, sign: str):
        field = self.field
        size = self.size
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        while field[x][y] != "□":
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
        field[x][y] = sign
        return field

    def check(self, sign: str):
        win_size = self.win_size
        field = self.field
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
                    if field[i - c][j + c] == field[i - c - 1][j + c + 1] == sign and (i - c - 1) > -1:
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

    def player_vs_player(self) -> tuple[str, any]:
        winner = str()
        p1 = self.p1_name
        p2 = self.p2_name
        while True:
            # player 1 turn
            self.print_field()
            print(p1 + " turn")
            sign = "X"
            self.player_turn(sign)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = p1
                break

            # player 2 turn
            self.print_field()
            print(p2 + " turn")
            sign = "0"
            self.player_turn(sign)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = p2
                break

            continue
        self.win_line = win_line
        return winner

    def player_vs_player_online(self, s, client_socket, status: int) -> tuple[str, any]:
        winner = str()
        p1 = self.p1_name
        p2 = self.p2_name
        while True:
            # host turn
            self.print_field()
            print(p1 + " turn")
            sign = "X"
            if status == 1:
                x, y = self.check_input()
                client_socket.send(bytes(str(x) + "|" + str(y), "utf-8"))
                self.player_online_turn(sign, x, y)
            elif status == 2:
                x, y = s.recv(1024).decode("utf-8").split("|")
                x, y = int(x), int(y)
                self.player_online_turn(sign, x, y)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = p1
                break

            # client turn
            self.print_field()
            print(p2 + " turn")
            sign = "0"
            if status == 2:
                x, y = self.check_input()
                s.send(bytes(str(x) + "|" + str(y), "utf-8"))
                self.player_online_turn(sign, x, y)
            elif status == 1:
                x, y = client_socket.recv(1024).decode("utf-8").split("|")
                x, y = int(x), int(y)
                self.player_online_turn(sign, x, y)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = p2
                break

            continue
        self.win_line = win_line
        return winner

    def player_vs_bot(self) -> tuple[str, any]:
        winner = str()
        p = self.p1_name
        b = self.p2_name
        while True:
            # player turn
            self.print_field()
            print(p + " turn")
            sign = "X"
            self.player_turn(sign)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = p
                break

            # bot turn
            self.print_field()
            print(b + " turn")
            sign = "0"
            self.bot_turn(sign)
            time.sleep(1)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = b
                break

            continue
        self.win_line = win_line
        return winner

    def bot_vs_bot(self) -> tuple[str, any]:
        winner = str()
        b1 = self.p1_name
        b2 = self.p2_name
        while True:
            # bot#1 turn
            self.print_field()
            print(b1 + " turn")
            sign = "X"
            self.bot_turn(sign)
            time.sleep(1)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = b1
                break

            # bot#2 turn
            self.print_field()
            print(b2 + " turn")
            sign = "0"
            self.bot_turn(sign)
            time.sleep(1)
            win_check, win_line = self.check(sign)
            if win_check == 1:
                winner = "Tie"
                break
            elif win_check == 2:
                winner = b2
                break

            continue
        self.win_line = win_line
        return winner


def start_singleplayer():
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
    win = ""
    mode, p1_name, p2_name = prompt()
    game = TicTacToe(size, win_size, p1_name, p2_name)
    game.create_field()
    if mode == 1:
        win = game.player_vs_player()
    elif mode == 2:
        win = game.player_vs_bot()
    elif mode == 3:
        win = game.bot_vs_bot()

    if win == "Tie":
        print("Tie")
        game.print_field()
    else:
        print(f"{win} WIN")
        game.print_winner()


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


# Host processing
def host_game(status, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)

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
    host_name = input("input your name: ")
    client_socket, address = s.accept()
    client_socket.send(bytes(host_name + "|" + str(size) + "|" + str(win_size), "utf-8"))

    client_name = client_socket.recv(20).decode("utf-8")

    game = TicTacToe(size, win_size, host_name, client_name)
    game.create_field()
    print("Game start!")
    while True:
        win = game.player_vs_player_online(s, client_socket, status)
        break

    if win == "Tie":
        print("Tie")
        game.print_field()
    else:
        print(f"{win} WIN")
        game.print_winner()
    client_socket.close()
    s.close()


# Client processing
def client_game(status, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    client_name = input("input your name: ")

    msg = s.recv(1024).decode("utf-8")
    host_name, size, win_size = msg.split("|")
    size, win_size = int(size), int(win_size)

    s.send(bytes(client_name, "utf-8"))

    game = TicTacToe(size, win_size, host_name, client_name)
    game.create_field()
    print("Game start!")
    while True:
        win = game.player_vs_player_online(s, None, status)
        break
    if win == "Tie":
        print("Tie")
        game.print_field()
    else:
        print(f"{win} WIN")
        game.print_winner()
    s.close()


def start():
    status = 0
    while True:
        try:
            game_mode = int(
                input(" Chose mode:\n1) multiplayer \n2) singleplayer \n"))
            while 1 > game_mode or game_mode > 2:
                print("Input correct data")
                game_mode = int(
                    input(" Chose mode:\n1) multiplayer \n2) singleplayer \n"))

            if game_mode != 2:
                status = int(input("1) Host game\n2) Connect to...\n"))
                while 1 > status or status > 2:
                    print("Input correct data")
                    status = int(input("1) Host game\n2) Connect to...\n"))
            break
        except ValueError:
            print("Input correct data")

    if game_mode == 2:
        start_singleplayer()

    if game_mode == 1 and status == 1:
        while True:
            try:
                ip = input("Input HOST IP: ")
                port = int(input("Input HOST port: "))
                host_game(status, ip, port)
                break
            except (ValueError, socket.gaierror, OverflowError, OSError):
                print("Input correct IP and port")

    elif game_mode == 1 and status == 2:
        while True:
            try:
                ip = input("Input HOST IP: ")
                port = int(input("Input HOST port: "))
                client_game(status, ip, port)
                break
            except (ValueError, socket.gaierror, OverflowError, OSError):
                print("Input correct IP and port")

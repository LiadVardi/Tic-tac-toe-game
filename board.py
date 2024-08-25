class Board:

    def __init__(self):
        self.data = list()
        for i in range(9):
            self.data.append('-')

    def print_board(self):
        print("\n|", self.data[0],"", self.data[1], "", self.data[2], "|")
        print("|", self.data[3], "", self.data[4], "", self.data[5], "|")
        print("|", self.data[6], "", self.data[7], "", self.data[8], "|\n")

    def print_defult(self):
        print("\n|", 1, "", 2, "", 3, "|")
        print("|", 4, "", 5, "", 6, "|")
        print("|", 7, "", 8, "", 9, "|\n")
    def add_x(self):
        flag = 1
        while flag:
            try:
                flag = 1
                while True:
                    x = int(input("Player X, where to mark the X (1-9): "))
                    if (x >= 1 and x <= 9):
                        if self.data[x - 1] == '-':
                            self.data[x - 1] = 'X'
                            break
                        else:
                            print("This place already taken, please choose other place!")
                    else:
                        print("Choose a number between 1-9.")
                flag = 0
            except:
                print("please insert only a whole number!")

        self.print_board()

    def add_o(self):
        flag = 1
        while flag:
            try:
                flag = 1
                while True:
                    o = int(input("Player O, where to mark the O (1-9): "))
                    if (o >= 1 and o <= 9):
                        if self.data[o - 1] == '-':
                            self.data[o - 1] = 'O'
                            break
                        else:
                            print("This place already taken, please choose other place!")
                    else:
                        print("Choose a number between 1-9.")
                flag = 0
            except:
                print("please insert only a whole number!")

        self.print_board()

    def who_win(board):
        if (board.data[0] == board.data[1] == board.data[2] != '-'):
            print(f"{board.data[1]} is the winner!")
            return 1

        elif (board.data[3] == board.data[4] == board.data[5] != '-'):
            print(f"{board.data[3]} is the winner!")
            return 1

        elif (board.data[6] == board.data[7] == board.data[8] != '-'):
            print(f"{board.data[6]} is the winner!")
            return 1

        elif (board.data[0] == board.data[3] == board.data[6] != '-'):
            print(f"{board.data[0]} is the winner!")
            return 1

        elif (board.data[1] == board.data[4] == board.data[7] != '-'):
            print(f"{board.data[1]} is the winner!")
            return 1

        elif (board.data[2] == board.data[5] == board.data[8] != '-'):
            print(f"{board.data[2]} is the winner!")
            return 1

        elif (board.data[0] == board.data[4] == board.data[8] != '-'):
            print(f"{board.data[0]} is the winner!")
            return 1

        elif (board.data[2] == board.data[4] == board.data[6] != '-'):
            print(f"{board.data[2]} is the winner!")
            return 1

        return 0


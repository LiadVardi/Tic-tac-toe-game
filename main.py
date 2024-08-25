from board import Board


print('\n Hello players,\n welcome to Tic-tac-toe game.')
print('\nthe rules: \n two players who take turns marking the spaces in a three-by-three grid with X or O. \n'
      ' The player who succeeds in placing three of their marks in a horizontal, vertical,\n or diagonal row  is'
      ' the winner.')
print('\n Player X is the starter.\n On each turn, the player chooses a number from 1 to 9 to mark the position he'
      ' wants to place his marker.')


board = Board()
board.print_defult()
board.add_x()
board.add_o()

count = 2
while True:
      if board.who_win():
            break
      board.add_x()
      count += 1
      if count == 9:
            print("\nthe board are full! \nno winner!")
            break
      if board.who_win():
            break
      board.add_o()
      count += 1


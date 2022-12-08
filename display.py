#Nathan Stettler, Austin Black
#CMSC-280: Project 4
#12/07/22

import os

class Display:
    'This class creates a display object that holds the current state of a tic tac toe game and methods to draw the board to the screen'

    def __init__(self):

        self.piece_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.board = self.create_board()


    def create_board(self):
        'This method creates a new list to hold the board grid and populates it'
        #These are the special characters used to draw the grid
        CROSS = chr(0x253C)
        VERTICAL =chr(0x2502)
        HORIZ = chr(0x2500)

        board = []
        
        for i in range(5):
            if i % 2 == 0:
                board.append([' ',' ',' ', VERTICAL, ' ', ' ', ' ',VERTICAL, ' ', ' ', ' '])
            else:
                board.append([HORIZ,HORIZ, HORIZ, CROSS, HORIZ, HORIZ, HORIZ, CROSS, HORIZ, HORIZ, HORIZ])

        return board


    def draw_board(self):
        'This method updates the board to its current state then prints it out'

        self.update_board()
        os.system( 'clear' )

        for list in self.board:
            for el in list:
                print(el, end='')
            print()



    def update_board(self):
        "This methods updates the board to the current location of the Xs and Os"

        #This dict holds coordinates for each possible piece position on the board
        pos_dict = {0:(0,1), 1:(0,5), 2: (0,9), 3:(2,1), 4:(2,5), 5: (2,9), 6:(4,1), 7:(4,5), 8: (4,9)}

        for i in range(9):
                self.board[pos_dict[i][0]][pos_dict[i][1]] = self.piece_list[i]
                







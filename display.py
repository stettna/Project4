'''This may need to be modifed some for sending so it prints to the user properly, but the basic pieces should be here '''


class Display:
    'This class creates a display object that holds to current state of the game and associated methods'

    def __init__(self):

        self.piece_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board = self.create_board()


    def create_board(self):
        'This method creates a new list to hold the board grid and populates it'

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

        for list in self.board:
            for el in list:

                print(el, end='')
            print()


    def update_board(self):
        "This methods updates the board to the current location of the Xs and Os"

        pos_dict = {0:(0,1), 1:(0,5), 2: (0,9), 3:(2,1), 4:(2,5), 5: (2,9), 6:(4,1), 7:(4,5), 8: (4,9)}

        for i in range(9):
            self.board[pos_dict[i][0]][pos_dict[i][1]] = self.piece_list[i]


    def detect_win( self ):
        """Detects if a player a won the game or not"""
        if any( 'X' == self.piece_list[a] == self.piece_list[b] == self.piece_list[c] 
	    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (1,4,7), (0,3,6), (2,5,8), (0,4,8), (2,4,6)] ):
            return True
        else:
            return False


def Game_Logic():
    ''' makes game do stuff correctly using Dispaly() "main()" '''
    d = Display()
    i = 0
    while True:
        try:
            player_move = int( input( "put piece where?: " ) )
            if (player_move > 8) or (player_move < 0):
                raise ValueError
        except ValueError:
            print( "You must enter an integer ( 0 - 8 )" )
            continue

        try:
            if i % 2 == 0:
                if (d.piece_list[player_move] == 'O') or (d.piece_list[player_move] == 'X'):
                    raise Exception
                d.piece_list[player_move] = 'X'
                d.draw_board()
                if d.detect_win():
                    print( "Player 1 wins!" )
                    break
                i += 1
            else:
                if (d.piece_list[player_move] == 'X') or (d.piece_list[player_move] == 'O'):
                    raise Exception
                d.piece_list[player_move] = 'O'
                d.draw_board()
                if d.detect_win():
                    print( "Player 2 wins!" )
                    break
                i += 1
        except Exception:
            print( "Slot already occupied!" )
            continue

#This is just for testing to see what the print out looks like
if __name__ == "__main__":
    Game_Logic()

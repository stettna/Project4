from server import detect_win
from display import Display

class TestTicTacToe:

    def setup_method(self):

        self.board = Display()

    def test_dect_win(self):
       
        self.board.piece_list = ['0','O','X','O','4','5','O','7','X']
        assert detect_win(self.board) == False
        	
        self.board.piece_list = ['O','O','O','X','4','5','X','7','X']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['X','X','X','O','4','5','O','7','X']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['0','O','X','O','O','O','X','7','X']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['0','O','X','X','X','X','O','7','X']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['O','O','X','O','O','5','O','7','O']
        assert detect_win(self.board) == True

        self.board.piece_list = ['','O','X','O','X','5','X','7','O']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['0','O','X','O','4','O','O','O','X']
        assert detect_win(self.board) == False 

        self.board.piece_list = ['0','O','X','O','O','5','O','O','X']
        assert detect_win(self.board) == True 

        self.board.piece_list = ['0','O','X','O','4','O','6','7','X']
        assert detect_win(self.board) == False 

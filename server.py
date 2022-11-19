import socket
from display import Display


CLIENT = []

def server():
    HOST = socket.gethostname()
    PORT = 5001

    sock = socket.socket()
    sock.bind(( HOST, PORT ))
    sock.listen()
    for i in range( 2 ):
        conn, addr = sock.accept()
        CLIENT.append( conn )
        num = i + 1
        CLIENT[i].send( str( num ).encode() )

    board = Display()

    CLIENT[0].send( ''.join(board.piece_list).encode() )
    CLIENT[1].send( ''.join(board.piece_list).encode() )

    while True:

        handle_move(board, 0)
        handle_move(board, 1)


    CLIENT[0].close()
    CLIENT[1].close()


def handle_move(board, num):
    
    data = CLIENT[num].recv(1024).decode()

    board.piece_list = list(data)  

    CLIENT[0].send( ''.join(board.piece_list).encode() )
    CLIENT[1].send( ''.join(board.piece_list).encode() )

 
def detect_win( self ):
    """Detects if a player a won the game or not"""
    if any( 'X' == self.piece_list[a] == self.piece_list[b] == self.piece_list[c] 
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (1,4,7), (0,3,6), (2,5,8), (0,4,8), (2,4,6)] ):
        return True
    else:
        return False


if __name__ == '__main__':
    server()

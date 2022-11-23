import socket
import time
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

    while True:
        try: 
            board = Display()
            count = [0]
            status = ['GIP']

            CLIENT[0].send( (''.join(board.piece_list)).encode() )
            CLIENT[1].send( (''.join(board.piece_list)).encode() )

            while True:
                handle_move(board, count, 0, status)
                if status[0] != 'GIP':	 
                    break
            
                handle_move(board, count, 1, status)
                if status[0] != 'GIP':	    
                    break

            if status[0] != 'CAT':
                break
        except IndexError:
            print("well somebody rage quit...")
            time.sleep( 3 )
            break

    print( "Shutting down clients" ) 
    CLIENT[0].close()
    CLIENT[1].close()
    print( "Shutting down server" )
    sock.close()

def handle_move(board,count,num, status):
 
    
    data = CLIENT[num].recv(1024).decode()
    board.piece_list = list(data)  
    count[0] += 1
    
    if detect_win(board):
       status[0] = 'P'+str(num+1)+ 'W'
    elif count[0] > 8:
        status[0] = 'CAT'
#print("Board: ", board.piece_list,status)
    CLIENT[0].send( (''.join(board.piece_list)+status[0]).encode() )
    CLIENT[1].send( (''.join(board.piece_list)+status[0]).encode() )

 
def detect_win(board):
    """Detects if a player a won the game or not"""

    if any( (('X' == board.piece_list[a] == board.piece_list[b] == board.piece_list[c]) or 
    ( 'O' == board.piece_list[a] == board.piece_list[b] == board.piece_list[c])) 
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (1,4,7), (0,3,6), (2,5,8), (0,4,8), (2,4,6)] ):
        return True
    else:
        return False


if __name__ == '__main__':
    server()

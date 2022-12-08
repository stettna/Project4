#Nathan Stettler, Austin Black
#CMSC-280: Project 4
#12/07/22

import socket
import time
from display import Display


CLIENT = []

def server():
    "This is a server that allows to players to connect and play tic tac toe"

    HOST = socket.gethostname()
    PORT = 5001
    
    sock = socket.socket()
    sock.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #recycle port number
    sock.bind(( HOST, PORT ))
    sock.listen()

    for i in range( 2 ):      #listen for only two clients, then continue
        conn, addr = sock.accept()
        CLIENT.append( conn )
        num = i + 1
        CLIENT[i].send( str( num ).encode() )

    #Start of game logic
    while True:
        try: 
            board = Display()
            count = [0]                #game state
            status = ['GIP']

            CLIENT[0].send( (''.join(board.piece_list)+status[0]).encode() )
            CLIENT[1].send( (''.join(board.piece_list)+status[0]).encode() )

            while True:   #handle move and check status as the game progresses
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
            time.sleep( 3)
            break

    shut_down(sock)


def handle_move(board,count,num, status):
    "This function handles the receiving of the game state from a client and the sending updated state to each client."
    
    data = CLIENT[num].recv(9).decode()
    board.piece_list = list(data) #unpack piece list
    count[0] += 1                 #increment game state
    board.draw_board()    

    if detect_win(board):
       status[0] = 'P'+str(num+1)+ 'W'
    elif count[0] > 8:
        status[0] = 'CAT'

    CLIENT[0].send( (''.join(board.piece_list)+status[0]).encode() )
    CLIENT[1].send( (''.join(board.piece_list)+status[0]).encode() )

 
def detect_win(board):
    "Detects if a player has won the game"

    if any( (('X' == board.piece_list[a] == board.piece_list[b] == board.piece_list[c]) or 
    ( 'O' == board.piece_list[a] == board.piece_list[b] == board.piece_list[c])) 
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (1,4,7), (0,3,6), (2,5,8), (0,4,8), (2,4,6)] ):
        return True
    else:
        return False


def shut_down(sock):
    "This function closes conections to the clients and shuts down the server."

    print( "Shutting down clients" ) 
    CLIENT[0].close()
    CLIENT[1].close()

    print( "Shutting down server" )
    sock.close()

if __name__ == '__main__':
    server()

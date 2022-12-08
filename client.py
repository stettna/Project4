import socket
import sys
import time
from termios import TCIFLUSH, tcflush
import display


def client():

    try:
        host_name = sys.argv[1]

    except:
        print("You must enter a host name")
        return

    host = host_name
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    player_no = client_socket.recv(1).decode()

    print( "WELCOME TO TIC TAC TOE\n" )
    print( "You are Player: " + str( player_no ) )
    print('''For this game, the standard Tic-Taac-Toe rule apply. Try to get three in a row.
To make a move, when it is your turn, enter the number shown in the positon you wish to plpace your piece. 
If a tie or Cat occurs, a new round begins''')
    time.sleep(3)


    while True:
        board = display.Display()
        status = ['GIP']      

        if player_no == "1":
            char = 'X'
            print("Waiting for opponent to join ... ")
            receive_data(client_socket, board, status)
            make_move(char, client_socket, board) 
            receive_data(client_socket, board, status)

        else:
            char = 'O'
            receive_data(client_socket, board, status)

        while True:
            try:
                print("Waiting for opponent to move ...")
                receive_data(client_socket, board, status)
                if not status[0] == 'GIP':
                    break

                make_move(char, client_socket, board)

                receive_data(client_socket, board, status)
                if not status[0] == 'GIP':
                    break

            except ValueError:
                sys.exit( "client disconnected" )
            except KeyboardInterrupt:
                sys.exit( "You quit!" )


        if status[0] == 'CAT':
            print( "CAT! Restarting game..." )
            time.sleep(3)
            continue

        elif str(player_no) == status[0][1]:
            print("YOU WON!")
        else:
            print("You Lost :( ")
        break	


def receive_data(client_socket, board, status):

    data = client_socket.recv(12).decode()
    if not data:
        sys.exit("error: client disconnected")
    board.piece_list = list(data[:9])
    board.draw_board()
    status[0] = data[9:12] 
   

def make_move(char, client_socket, board):

    tcflush(sys.stdin, TCIFLUSH)
    move = input("Make your next move: ")

    while not is_valid_play(move, board):
        tcflush(sys.stdin, TCIFLUSH)
        move = input("Invalid move! Try again: ")

    board.piece_list[int(move)-1] = char
    client_socket.send(''.join(board.piece_list).encode())


def is_valid_play(move, board):

    if (move.isdigit() and int(move) > 0 and int(move) <= 9):
        if board.piece_list[int(move)-1].isdigit():
            return True

    return False



if __name__ == '__main__':
    client()

import socket
import sys
from termios import TCIFLUSH, tcflush
import display

board = display.Display()

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

    player_no = client_socket.recv(1024).decode()

    print( "WELCOME TO TIC TAC TOE\n" )
    print( "You are Player: " + str( player_no ) )

    if player_no == "1":
        char = 'X'
        print("Waiting for opponent ... ")
        receive_data(client_socket)
        make_move(char, client_socket) 
        receive_data(client_socket)

    else:
        char = 'O'
        receive_data(client_socket)

    while True:

        print("Waiting for opponent to move ...")
        receive_data(client_socket)
        make_move(char, client_socket)
        receive_data(client_socket)


def receive_data(client_socket):

    data = client_socket.recv(1024).decode()
    board.piece_list = list(data)

    board.draw_board()


def make_move(char, client_socket):

    tcflush(sys.stdin, TCIFLUSH)
    move = input("Make your next move: ")

    while not is_valid_play(move):
        tcflush(sys.stdin, TCIFLUSH)
        move = input("Invalid move! Try again: ")

    board.piece_list[int(move)] = char
    client_socket.send(''.join(board.piece_list).encode())


def is_valid_play(move):

    if (move.isdigit() and int(move) >= 0 and int(move) < 9):
        if board.piece_list[int(move)] == '!':
            return True

    return False



if __name__ == '__main__':
    client()

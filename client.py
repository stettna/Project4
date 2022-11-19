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
        print("Waiting for opponent ... ")
        receive_data(client_socket)
        char = 'X'
    else:
        char = 'O'

    while True:

        if player_no == "1":
            make_move(char, client_socket)
            receive_data()

        if player_no == "2":
            receive_data(client_socket)
            make_move(char, client_socket)


def receive_data(client_socket):

    data = client_socket.recv(1024).decode()
    board.piece_list = data.split()
    board.update_board()


def make_move(char, client_socket):

    tcflush(sys.stdin, TCIFLUSH)
    move = input("Make your next move: ")

    while not is_valid_play(move):
        tcflush(sys.stdin, TCIFLUSH)
        move = input("Invalid move! Try again: ")

    board.piece_list[move] = char
    client_socket.send(''.join(board.piece_list).encode())


def is_valid_play(move):

    if (move.is_digit() and int(move) >= 0 and int(move) < 9):
        if board.piece_list[move] == ' ':
            return True

    return False



if __name__ == '__main__':
    client()

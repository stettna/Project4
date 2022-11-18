import socket
import sys
from termios import TCIFLUSH, tcflush

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

    while True:
        if player_no == "1":

            tcflush(sys.stdin, TCIFLUSH)
            message = input( "->" )
            client_socket.send( message.encode() )
            data = client_socket.recv(1024).decode()
            print( "recieved: " + data )

        if player_no == "2":
            data = client_socket.recv(1024).decode()
            print( "recieved: " + data )
            tcflush(sys.stdin, TCIFLUSH)
            message = input( "->" )
            client_socket.send( message.encode() )


if __name__ == '__main__':
    client()

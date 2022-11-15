import socket
import sys

def client():

    try:
        host_name = sys.argv[1]
    except:
        print("You must enter a host name")
        return

    host = host_name
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input('-> ')

    while message.lower().strip() != 'quit':

        client_socket.send( message.encode() )

        data = client_socket.recv(1024).decode()

        print( "recieved from server: " + data )

        message = input( '-> ')

    client_socket.close()


if __name__ == '__main__':
    client()

import socket

clients = list()

def server():
    HOST = socket.gethostname()
    PORT = 5001
    CLIENT = []

    sock = socket.socket()
    sock.bind(( HOST, PORT ))
    sock.listen()
    for i in range( 2 ):
        conn, addr = sock.accept()
        CLIENT.append( conn )
        num = i + 1
        CLIENT[i].send( str( num ).encode() )

#    for i in range( 2 ):
#       print( CLIENT[i] )

    while True:
        data = CLIENT[0].recv(1024).decode()
        print( "recieved from player 1: " + data + " | sending to player 2." )
        CLIENT[1].send( data.encode() )

        data = CLIENT[1].recv(1024).decode()
        print( "recieved from player 2: " + data + " | sending to player 1." )
        CLIENT[0].send( data.encode() )

        if data == "quit":
            ...

    CLIENT[0].close()
    CLIENT[1].close()

if __name__ == '__main__':
    server()

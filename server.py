import socket
import selectors
import types

selector = selectors.DefaultSelector()
players = []


def server():

    host = socket.gethostname()
    port = 5000


    server_socket = socket.socket()
    server_socket.bind( (host, port) )
    server_socket.listen(2)

    server_socket.setblocking(False)
    selector.register(server_socket, selectors.EVENT_READ, data=None)


    while True:

        events = selector.select(timeout=None)

        for key, mask in events:

                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    serve_connection(key, mask)


    server_socket.close()


def accept_wrapper(socket):


    conn, address = socket.accept()
    print("Connection from: " + str(address))

    conn.setblocking(False)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(addr=address, inb=b"", outb=b"")

    players.append((socket,data))

    selector.register(conn, events, data=data)


def serve_connection(key, mask):

    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read

        if recv_data:
            handle_data(key, recv_data)

        else:
            print(f"Closing connection to {data.addr}")
            selector.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


def handle_data(key, recv_data):

    for player in players:
        player[1].outb += recv_data




if __name__ == '__main__':
    server()

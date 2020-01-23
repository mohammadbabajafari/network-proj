import json as JSON
import socket
import time
from concurrent.futures.thread import ThreadPoolExecutor

IP_ADDRESS = 'localhost'
PORT = 10000


# Create a TCP/IP socket

def folan():
    for i in range(10):
        print(i)
    time.sleep(20)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (IP_ADDRESS, PORT)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(100)
    with ThreadPoolExecutor(max_workers=8) as t:
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            fu = t.submit(handle_received, sock, connection, client_address)


def handle_received(sock: socket.socket, connection: socket.socket, client_address: str):
    rcv = connection.recv(5)
    print(rcv)
    data = b''
    json = None

    while rcv:
        data += rcv
        rcv = connection.recv(5)
        print(rcv)

    try:
        json = JSON.loads(data)
    except ValueError as e:
        # client_address.split(':')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(client_address[0], 10000)
        sock.sendall(b'not valid input')
        return
    typ = json.get('type')
    if typ == 'B':
        pass
    elif typ == 'Q':
        pass
    elif typ == 'QA':
        pass

    # parse data
    # handle data
    # if data_type B -> handle broadcast
    # if data_type Q -> handle query
    # if data_type QA -> handle query answer


if __name__ == '__main__':
    main()

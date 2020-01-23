import json as JSON
import socket
import time
from concurrent.futures.thread import ThreadPoolExecutor

import settings
from json_utils import handle_json
from message_types import MessageType

IP_ADDRESS = settings.MY_IP_ADDRESS
PORT = settings.PUBLIC_PORT


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
    sock.listen(1)
    with ThreadPoolExecutor(max_workers=8) as t:
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            print(f'{client_address} connected.')
            fu = t.submit(handle_received, sock, connection, client_address)


def handle_received(sock: socket.socket, connection: socket.socket, client_address: str):
    rcv = connection.recv(settings.BUFFER_SIZE)
    print(rcv)
    data = b''
    json = None

    while rcv:
        data += rcv
        rcv = connection.recv(settings.BUFFER_SIZE)
        print(rcv)

    try:
        json = JSON.loads(data)
        result = handle_json(json)
    except ValueError as e:
        result = dict(
            type=MessageType.ERROR,
            status=500,
            content=dict(
                text='Received data is not json',
            )
        )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((client_address[0], settings.PUBLIC_PORT))
        sock.sendall(str.encode(JSON.dumps(result)))


    # parse data
    # handle data
    # if data_type B -> handle broadcast
    # if data_type Q -> handle query
    # if data_type QA -> handle query answer


if __name__ == '__main__':
    main()

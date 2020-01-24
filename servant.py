import json as _json
import socket
from concurrent.futures.thread import ThreadPoolExecutor

import settings
from init import initial_db
from json_utils import handle_json
from message_types import MessageType

IP_ADDRESS = settings.MY_IP_ADDRESS
PORT = settings.PUBLIC_PORT
mongo_db = initial_db()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (IP_ADDRESS, PORT)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(10)
    with ThreadPoolExecutor(max_workers=8) as t:
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            print(f'{client_address} connected.')
            fu = t.submit(handle_received, sock, connection, client_address)


def handle_received(sock: socket.socket, connection: socket.socket, client_address: tuple):
    from common_utils import send_p2p
    rcv = connection.recv(settings.BUFFER_SIZE)
    print(rcv)
    data = b''
    json = None

    while rcv:
        data += rcv
        rcv = connection.recv(settings.BUFFER_SIZE)
        print(rcv)

    try:
        json = _json.loads(data)
        result = handle_json(json, client_address)
    except ValueError as e:
        send_p2p(dict(text='Received data is not json'), MessageType.ERROR, 500, client_address)


if __name__ == '__main__':
    main()

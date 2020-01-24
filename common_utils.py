import json as _json
import socket

import settings
from data import Data
from message_types import MessageType


def base_send(data: dict, address: tuple):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip_address = address[0]
    server_address = (server_ip_address, settings.PUBLIC_PORT)
    sock.connect(server_address)
    sock.sendall(str.encode(_json.dumps(data)))
    sock.close()


def send_p2p(content: dict, typ: str, status: int, address):  # msg acc error qa   send to one specific   content type

    data = {'type': typ, 'status': status, 'content': content}
    base_send(data, address)


def send_flood(content: dict, typ: str, status: int, uuid: str):  # q,b send to all  type content uuid

    data = {'type': typ, 'status': status, 'content': content, 'id': uuid}

    f_list = list()

    if typ == MessageType.QUERY:
        f_list = Data.get_followings()

    elif typ == MessageType.BROADCAST:
        f_list = Data.get_followers()

    for ip in f_list:
        base_send(data, (ip,))

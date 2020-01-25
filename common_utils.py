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
    if isinstance(address, str):
        address = (address, settings.PUBLIC_PORT)
    data = {'type': typ, 'status': status, 'content': content}
    base_send(data, address)


def send_flood(content: dict, typ: str, status: int, uuid: str,
               black_list: list = []):  # q,b send to all  type content uuid

    data = {'type': typ, 'status': status, 'content': content, 'id': uuid}

    f_list = list()

    if typ == MessageType.QUERY:
        f_list = Data.get_followings()

    elif typ == MessageType.BROADCAST:
        f_list = Data.get_followers()

    elif typ == MessageType.LEAVE:
        f_list = Data.get_followers() + Data.get_followings()

    for bl in black_list:
        try:
            f_list.remove(bl)
        except ValueError as e:
            pass

    for ip in f_list:
        base_send(data, (ip,))

    return f_list

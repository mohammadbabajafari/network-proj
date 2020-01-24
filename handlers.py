from common_utils import send_flood
from data import Data
from send_utils import send_accept


def handle_accept(json: dict, address: tuple, *args, **kwargs):
    pass


def handle_error(json: dict, address: tuple, *args, **kwargs):
    pass


def handle_broadcast(json: dict, address: tuple, *args, **kwargs):
    if not Data.has_flood_received(json.get('id')):
        Data.add_floods_received(json.get('id'))
        send_flood(json.get('content'), json.get('type'), json.get('status'), json.get('id'))


def handle_query(json: dict, address: tuple, *args, **kwargs):
    if not Data.has_flood_received(json.get('id')):
        Data.add_floods_received(json.get('id'))
        send_flood(json.get('content'), json.get('type'), json.get('status'), json.get('id'))


def handle_query_answer(json: dict, address: tuple, *args, **kwargs):
    pass


def handle_follow(json: dict, address: tuple, *args, **kwargs):
    Data.add_follower(address[0])
    send_accept(address)


def handle_message(json: dict, address: tuple, *args, **kwargs):
    send_accept(address)

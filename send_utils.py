import datetime
import uuid

from common_utils import send_flood, send_p2p
from data import Data
from db_utils import add_uuid_to_db
from message_types import MessageType
from settings import PUBLIC_PORT, MY_IP_ADDRESS, TTL


def send_accept(address: tuple):
    send_p2p({}, MessageType.ACCEPT, 100, address)  # todo: provide content


def send_follow(ip: str):
    content = {}  # todo: provide content
    tupleIp = (ip, PUBLIC_PORT)
    send_p2p(content, MessageType.FOLLOW, 150, tupleIp)


def send_broadcast(message: str):
    time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    content = {'text': message, 'timestamp': time, 'src': MY_IP_ADDRESS}
    uuid_str = str(uuid.uuid4())
    add_uuid_to_db(uuid_str, message, time)
    send_flood(content, MessageType.BROADCAST, 250, uuid_str)


def send_query(message: str):
    content = {'text': message, 'timestamp': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
               'src': MY_IP_ADDRESS, 'TTL': TTL}
    uuid_str = str(uuid.uuid4())
    send_flood(content, MessageType.QUERY, 270, uuid_str)


def send_query_answer(content: dict, address: str):
    Data.set_waiting_as_answered(content['uuid'])
    send_p2p(content, MessageType.QUERY_ANSWER, 300, address)

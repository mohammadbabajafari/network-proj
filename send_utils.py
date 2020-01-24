from common_utils import send_p2p
from message_types import MessageType


def send_accept(address: tuple):
    send_p2p({}, MessageType.ACCEPT, 100, address) # todo: provide content

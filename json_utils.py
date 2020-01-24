from message_types import HANDLER


def handle_json(json: dict, address: tuple):
    typ = json.get('type')
    HANDLER[typ](json, address)

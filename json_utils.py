from message_types import MessageType, HANDLER


def handle_json(json: dict, address: tuple):
    typ = json.get('type')
    HANDLER[typ](json, address)

    # if typ == MessageType.ERROR:
    #     pass
    # elif typ == MessageType.BROADCAST:
    #     pass
    # elif typ == MessageType.FOLLOW:
    #     pass
    # elif typ == MessageType.QUERY:
    #     pass
    # elif typ == MessageType.QUERY_ANSWER:
    #     pass


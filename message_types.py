class MessageType:
    ERROR = 'E'
    BROADCAST = 'B'
    QUERY = 'Q'
    QUERY_ANSWER = 'QA'
    FOLLOW = 'F'
    ACCEPT = 'A'
    MESSAGE = 'M'

from handlers import *
attrs = list(filter(lambda x: x[:2] != '__', dir(MessageType)))
HANDLER = {}
for attr in attrs:
    HANDLER[eval('MessageType.'+attr)] = eval('handle_'+attr.lower())

from datetime import timedelta

BUFFER_SIZE = 1024
PUBLIC_PORT = 10000
MY_IP_ADDRESS = 'localhost'

MONGO_URL = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'network'
MONGO_COL_NAME = 'broadcast_messages'

TTL = 5
TTW = timedelta(minutes=3)

try:
    from local_settings import *
except ImportError as e:
    pass

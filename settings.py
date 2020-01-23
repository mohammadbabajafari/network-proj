BUFFER_SIZE = 1024
PUBLIC_PORT = 10000
MY_IP_ADDRESS = 'localhost'


try:
    from local_settings import *
except ImportError as e:
    pass

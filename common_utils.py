import socket
import sys
import settings
import json as JSON

def base_send(data: dict , address: tuple):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverIpAddress = address[0]
    server_address = (serverIpAddress, settings.PUBLIC_PORT)
    sock.connect(server_address)
    sock.sendall(str.encode(JSON.dumps(data)))
    sock.close()

def send_p2p(content: str, typ: str, address): #msg acc error qa   send to one specific   contetn type

    data = {'type' : typ, 'content' : content}
    base_send(data, address)

def send_flood(content: str, typ: str, uuid: str): #q,b send to all  type contetn uuid
    
    data = {'type' : typ, 'content' : content, 'uuid' : uuid}

    #get followers or followings
    if typ == 'Q':
        f_list = []

    elif typ == 'B':
        f_list = []
        
    for ip in f_list:
        base_send(data, ip)

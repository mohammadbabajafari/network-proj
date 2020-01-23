import socket
import sys
import settings
import json as JSON

def send(data: dict , address: tuple):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverIpAddress = address[0]
    server_address = (serverIpAddress, settings.PUBLIC_PORT)
    sock.connect(server_address)
    sock.sendall(str.encode(JSON.dumps(data)))
    sock.close()

def sendMsg(address, data: dict):
    
import socket 
import threading
import time 

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5053
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


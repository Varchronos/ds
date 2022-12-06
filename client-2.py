from termcolor import colored
import socket 
import threading
import time 

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5053
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
connected =  False
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def chat():
    connected = True     
    while connected:
        msg = input(str("-->"))
        if(msg == DISCONNECT_MSG):
            client.send(bytes(DISCONNECT_MSG,FORMAT))
            connected = False
        else:
            client.send(bytes(msg, FORMAT))
        # msg =(client.recv(1024).decode(FORMAT))
        # print(colored("[SERVER]",'green') + f": {msg}")
        # print(f'\033[1A' + "[SERVER]: {msg}" + '\033[K')
    
    if(connected == False):
        exit()


def start():
    try:
        client.connect((SERVER, PORT))
    except:
        print(colored("SERVER IS OFFLINE!!!", 'magenta') + " Closing client...")
        exit()

    msg =(client.recv(1024).decode(FORMAT))
    print(colored("[SERVER]",'green') + f": {msg}")
    while True:
        chat()
        
    
        

print(colored("[STARTING]",'red') + "client is starting...")
start()

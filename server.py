from termcolor import colored
from datetime import datetime
import socket 
import threading
import time 

HEADER = 32
PORT = 5053
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send(bytes("you have joined", FORMAT))
    connected = True

    while connected:
            msg = conn.recv(1024).decode(FORMAT)
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            if msg:
                if(msg == DISCONNECT_MSG):
                    connected = False
                    break

            print(colored(f"[CLIENT {addr}]", 'green') + f": {msg}" + colored(date_time.strftime(" [%H:%M:%S]"),'yellow'))
            # msg = input(str("-->"))
            # conn.send(bytes(msg, FORMAT))


    print("\n" + colored(f"[CLIENT {addr} has disconnected]", 'red'))
    conn.close()

def start():
    server.listen()
    print(colored("[LISTENING]",'red') + f"Server is Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread  = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(colored("[ACTIVE CONNECTIONS]", 'yellow') + f"{threading.active_count() - 1}\n")

print( colored("[STARTING]",'red') + "server is starting...")
start()

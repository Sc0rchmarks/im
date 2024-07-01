import socket
import os
from threading import Thread


ip = input("Please enter the listening IP: ")
port = input("Please enter the port number (Default = 42069): ")

if not port:
    port = int(42069)
else:
    try:        
        int(port)
    except:
        print("You must specify a numerical port number!")
        exit()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_ip = ip
    server_port = int(port)
    seperator_token = "<SEP>"

    client_sockets = set()
    
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((server_ip, server_port))
    server.listen(199)
    print(f"Listening on {server_ip}:{port}")
except socket.error as e:
    print(f"Error creating socket: {e}")
    
def listen(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"!!! Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(seperator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())
while True:
    client_socket, client_address = server.accept()
    print(f"+ {client_address} connected.")
    client_sockets.add(client_socket)

    t = Thread(target=listen, args=(client_socket,))
    t.daemon = True
    t.start





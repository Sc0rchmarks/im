import socket
import os
from threading import Thread
import configLib

users = {}

if not configLib.checkconfig():
    configLib.createconfig()
#ip = input("Please enter the listening IP: ")
ip = configLib.checkValue("ip")
#port = input("Please enter the port number (Default = 42069): ")
port = configLib.checkValue("port")
if not port:
    port = int(42069)
else:
    try:        
        port = int(port)
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
def commands():
    while True:
        to_send = input("> ")
        if to_send.lower() == 'q':
            socket.close()
            exit()
        else:
            return to_send
def listen(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:

        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()

        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(seperator_token, ": ")
            print("Message recieved")
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            # iterate over all connected sockets


        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())
            print("Message sent")


while True:
    client_socket, client_address = server.accept()
    print(f"+ {client_address} connected.")
    client_sockets.add(client_socket)
    client_socket.send(configLib.checkValue("motd").encode())
    try:
        name =client_socket.recv(1024).decode()
        users[name] = client_address[0]

        commands()
    except:
        client_socket.send("There is already a user with that name on the server. Please choose a different one & reconnect").encode()


t = Thread(target=listen, args=(client_socket,))
t.daemon = True
t.start()










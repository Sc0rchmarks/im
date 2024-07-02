import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = Fore.LIGHTBLACK_EX

seperator_token = "<SEP>"
name = input("Enter your username: ")
s = socket.socket()

    
var1 = input(f"Is the name {name} correct? [Y|N]: ").lower()
while True:
    if var1 == "y":
        break
    elif var1 == "n":
        name = input("Enter your username: ")
    else:
         print("You must select a valid option! ")
        
def connect():
    while True:
        srv_host = input("What IP would you like to connect to?")
        srv_port = input("What port should the client look for? (Default is 42069)")
        if not srv_port:
            srv_port = int(42069)
        elif 65535 < int(srv_port) or int(srv_port) < 0:
            print("You must use a valid port number [1-65535]")
        else:
            try:
                int(port)
            except:
                print("You must specify a valid port number!")    
        try:
            s.connect((srv_host, srv_port))
            break
        except socket.error as e:
            print(f"Socket error: {e}")



connect()  

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send = input("Enter your message >")
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    #date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color} {name}{seperator_token}{to_send}{Fore.RESET}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()
  


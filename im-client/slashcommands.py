import re

cmdRE = re.compile("/*\\s")

def listen_for_cmds(msgToSend):
    while True:
        if cmdRE.match(msgToSend):
            cmd = cmdRE.match(msgToSend)
            if cmd.group() == "/q " or "/quit " or "/exit ":
                print("\nGoodbye !!\n")
                exit()
            
            
                

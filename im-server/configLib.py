import re

def createconfig():
    with open("config.yml", "w") as f:
        f.write("ip: 0.0.0.0\nport: 42069\nmotd: \"Thank you for connecting! Welcome $username!\"")
        f.close()

def checkconfig():
    try:
        with open("config.yml", "r") as f:
            f.close()
            return True
    except:
        return False
def checkValue(value):
    if not checkconfig():
        createconfig()
    with open("config.yml", "r") as f:

        try:
            config = f.read()
            c = re.compile(f"{value}: .*")
            m = c.search(config)
            t = m.group().split(f"{value}: ")
            f.close()

            # print(f[1])
            return t[1]

        except:
            print(f"Value {value} could not be found! Make sure the config file is correct!")
def motdProcess(motd):
    re.compile("")




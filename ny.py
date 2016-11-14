import time
import sys

line = "y"
while line[0] == ("y") not in ("n"):
    user = "123"

    login = input("Hej. Vad är ditt namn?: ")

    if login == user:
        print("Laddar...")
        time.sleep(3)
        print("Välkommen " + user + "!")
    else:
        print("Laddar...")
        time.sleep(3)
        print("Nähädu, det här var fel, din dumstrut!")
        line = input("Vill du försöka igen? (y/n): ")

def exit():
    sys.exit()

while line[0] == ("n"):
    print("Hejdå!")
    exit()
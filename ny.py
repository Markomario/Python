import time
import sys

progge = "y"
line = "y"
while progge[0] == ("y") not in ("n"):
    user = "Markus"

    login = input("Hej. Vad är min mästares namn?: ")

    if login == user:
        print("Laddar...")
        time.sleep(3)
        while line[0] == ("y") not in ("n"):
            kalk = input("Välkommen " + user + "!\nHur vill du räkna?\n+\n-\n*\n/\n: ")
            number1 = int(input("Välj det första nummret som du vill räkna med: "))
            number2 = int(input("Välj det andra nummret som du vill räkna med: "))

            if kalk == "+":
                print("Laddar....")
                time.sleep(3)
                print(user + ", summan blir:", number1 + number2)
                line = input("Vill du starta om programmet? (y/n): ")
            elif kalk == "-":
                print("Laddar....")
                time.sleep(3)
                print(user + ", differensen blir:", number1 - number2)
                line = input("Vill du starta om programmet? (y/n): ")
            elif kalk == "*":
                print("Laddar....")
                time.sleep(3)
                print(user + ", produkten blir:", number1 * number2)
                line = input("Vill du starta om programmet? (y/n): ")
            elif kalk == "/":
                print("Laddar....")
                time.sleep(3)
                print(user + ", kvoten blir:", number1 / number2)
                line = input("Vill du starta om programmet? (y/n): ")
            else:
                time.sleep(2)
                line = input("Något verkar ha gått snett nu. Vill du försöka igen? (y/n): ")


    else:
        print("Laddar...")
        time.sleep(3)
        print("Nähädu, det här var fel, din dumstrut!")
        progge = input("Vill du försöka igen? (y/n): ")

while line == "n":
    progge = "n"

def exit():
    sys.exit()

while progge[0] == ("n"):
    print("Ok, ha en bra dag!")
    time.sleep(2)
    print("Stänger av nu.")
    exit()
import sys
import time
def exit():
    sys.exit()

progge = "y"
line = "j"

while progge [0] == ("y") not in ("n"):
    user = "Markus"

    loggin = input("Vad heter annändaren på denna datorn?: ")

    if loggin == "Markus":
        line = "j"
        while line[0] == ("j") not in ("n"):
            kalk = input("Hej igen " + user + "!\nHur vill du räkna?\n+\n-\n*\n/\n: ")
            number1 = int(input("Välj det första nummret som du vill räkna med: "))
            number2 = int(input("Välj det andra nummret som du vill räkna med: "))
            if kalk == "+":
                print("Laddar....")
                time.sleep(3)
                print(user + ", summan blir:", number1 + number2)
                line = input("Vill du starta om programmet? (j/n): ")
            elif kalk == "-":
                print("Laddar....")
                time.sleep(3)
                print(user + ", differensen blir:", number1 - number2)
                line = input("Vill du starta om programmet? (j/n): ")
            elif kalk == "*":
                print("Laddar....")
                time.sleep(3)
                print(user + ", produkten blir:", number1 * number2)
                line = input("Vill du starta om programmet? (j/n): ")
            elif kalk == "/":
                print("Laddar....")
                time.sleep(3)
                print(user + ", kvoten blir:", number1 / number2)
                line = input("Vill du starta om programmet? (j/n): ")
            else:
                print("Laddar...")
                time.sleep(2)
                line = input("Något verkar ha gått snett nu. Vill du försöka igen? (j/n): ")
        if line == ("n"):
            progge = "n"
    else:
        print("nu gick det fel")
        progge = input("vill du avsluta?")

while progge == ("n"):
    print("Ok, ha en bra dag!")
    time.sleep(2)
    print("Stänger av nu...")
    exit()
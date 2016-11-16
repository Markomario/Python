import sys
import time
def exit():
    sys.exit()

progge = "y"
line = "j"

while progge [0] == ("y") not in ("n"):
    user = "Markus"

    loggin = input("Vad heter min mästare?: ")

    if loggin == "Markus":
        line = "j"
        while line[0] == ("j") not in ("n"):
            print("Laddar...")
            time.sleep(3)
            kalk = input("Mästare " + user + "!\nHur vill du räkna?\nAddition,\nSubbtraktion,\nMultiplikation,\neller Divition?\n(Skriv tecknet, inte ordet)\n: ")
            number1 = int(input("Välj det första nummret som du vill räkna med: "))
            number2 = int(input("Välj det andra nummret som du vill räkna med: "))
            if kalk == "+":
                print("Laddar....")
                time.sleep(3)
                print(user + ", summan blir:", number1 + number2)
                line = input("Vill du räkna igen? (j/n): ")
            elif kalk == "-":
                print("Laddar....")
                time.sleep(3)
                print(user + ", differensen blir:", number1 - number2)
                line = input("Vill du räkna igen? (j/n): ")
            elif kalk == "*":
                print("Laddar....")
                time.sleep(3)
                print(user + ", produkten blir:", number1 * number2)
                line = input("Vill du räkna igen? (j/n): ")
            elif kalk == "/":
                print("Laddar....")
                time.sleep(3)
                print(user + ", kvoten blir:", number1 / number2)
                line = input("Vill du räkna igen? (j/n): ")
            else:
                print("Laddar...")
                time.sleep(2)
                line = input("Något verkar ha gått snett. Vill du försöka igen? (j/n): ")
        if line == ("n"):
            progge = "n"
    else:
        print("Du är inte min mästare!")
        progge = input("Vill du försöka att logga in igen?")

while progge == ("n"):
    print("Ok, ha en bra dag!")
    time.sleep(1)
    print("Stänger av nu...")
    time.sleep(2)
    exit()
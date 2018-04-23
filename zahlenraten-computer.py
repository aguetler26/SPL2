# zufallszahlen-raten-computer.py

rand = 17
max = 200
gewonnen = False
versuche = 0

print("Zufallszahlen-Raten: der Computer wird versuchen, die Zahl zu erraten.")
zahl = max / 2
while(gewonnen == False):
    versuche += 1
    if (zahl == rand):
        print("probiere mit", zahl)
        gewonnen = True
    else:
        if (zahl > rand):
            print("zahl ist zu gross...")
            zahl = int(zahl - zahl/2)
            print("probiere mit", zahl)
        else:
            print("zahl ist zu klein...")
            zahl = int(zahl + zahl/2)
            print("probiere mit", zahl)
    if versuche >20:
        break

print("Versuche:", versuche)
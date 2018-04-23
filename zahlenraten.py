# zahlenraten.py

max = 200
zufallszahl = 11
gewonnen = False
versuche = 0
print("Zufallszahlen-raten: bitte eine Zahl zwischen 1 und", max, "eingeben")

while(gewonnen == False):
    zahl = input("Welche Zahl? ")
    zahl = int(zahl)
    if (zahl == zufallszahl):
        gewonnen = True
    if (zahl < zufallszahl):
        print("----")
    if (zahl > zufallszahl):
        print("++++")

print("Bravo - du hast die Zahl in", versuche, "Versuchen erraten")


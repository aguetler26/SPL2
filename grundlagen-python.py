# grundlagen-python.py
import random
# Kommentare erfolgen mit hashtag

# Ausgabe von Daten
print("Hallo World")

# Variable definieren (kann ohne Typ erfolgen)
heimat = "Erde"

# Mehrere Variable werden mit , getrennt
print(heimat, "an World: ", "Hallo!")

# Eingabe / liest Text(!) von der Konsole ein
wer = input("Und wer bist du? ")

# und gibt den Text wieder aus
if (wer == "ich"):
    print ("Hallo Du!")
else:
    print ("Hallo", wer)

lieblingszahl = input("Was ist deine Lieblingszahl? ")
print("Super, ich mag die Zahl", lieblingszahl)
print("Aber die coolere Zahl", int(lieblingszahl)+10, "mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)

siege_computer = 0
siege_ich = 0

for runde in range(1, runden+1):
    sieger = ""
    # zufallszahl erzeugen
    zufallszahl = random.randint(1,6)
    # ist zufallszahl 1,3 oder 5: bin ich der sieger
    # sonst ist der computer der sieger
    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger = "ich"
        siege_ich += 1
    else:
        sieger = "computer"
        siege_computer += 1
    print("Runde", runde, "von", runden, ": Sieger:", sieger, ": gewuerfelt wurde:", zufallszahl)

if (siege_ich > siege_computer):
    print("Du gewinnst!")
elif (siege_computer > siege_ich):
    print("Du verlierst!")
else:
    print("Unentschieden")
print("game over.")

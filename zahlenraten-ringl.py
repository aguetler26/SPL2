#zahlenraten.py
#Sicht vom Benutzer
import random
max = 200
min = 1
gewonnen = False

zufallszahl = random.randint(min,max)
entscheidung = input ("Willst du ein Spiel spielen?    ja    oder     nein")
if(entscheidung == "nein"):
    print("Schade")

else:
    print("Auf gehts")
    print("Bitte rate eine zahl zwischen 1 und 200 :-)")
    while(gewonnen == False):
        Benutzerzahl = input(" ")
        Benutzerzahl = int(Benutzerzahl)
        if(Benutzerzahl == zufallszahl):
            gewonnen == True 
            print("Richtig du hast die Zahl erraten")
            break
        elif(Benutzerzahl <= zufallszahl):
            print ("Die Zufallszahl ist größer als deine Zahl")
        else:
            print ("Deine Zahl ist größer als meine")
            
print("Du hast gewonnen!!")
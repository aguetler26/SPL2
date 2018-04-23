# Zahlenraten.py

#maxzahl = input("Geben Sie die höchste Zahl ein!")
maxzahl = 100
#zahl = input("Geben Sie nun jene Zahl ein, die der Computer erraten soll.")
#print(zahl)
zahl = 67

erraten = False
Czahl = maxzahl/2
Czahl = int(Czahl)
versuche = 0

last = maxzahl
rechnung = Czahl
    
while(erraten == False):
    versuche += 1
    print(rechnung)
    if(rechnung < zahl):
        rechnung = rechnung + int(rechnung/2)
    elif(rechnung > zahl):
        rechnung = rechnung - int(rechnung/2)
    elif(rechnung == zahl):
        erraten = True 
    
    if(versuche > 10): 
        break
print("Der Computer benötigte", versuche, "Versuche um die Zahl", zahl, "zu erraten.")
import random
#1. Wir setzen die Obergrenze der Zufahlszahl anhand des Schwierigkeitsgrades
print("Herzlich Wilkommen zum Zahlenraten! Wähle eine Schwierigkeit: 1 = 1-10, 2 = 1-25, 3 = 1-50")
schwierigkeit = int(input("Treffe deine Wahl: 1,2 oder 3: "))
obergrenze = 10
if schwierigkeit == 2:
    obergrenze = 25
if schwierigkeit == 3:
    obergrenze = 50

#2. Wir generieren eine heimliche Zufallszahl zwischen 1 und der Obergrenze
zufallszahl = random.randint(1,obergrenze)
print("Ich habe mir eine Zahl zwischen 1 und " + str(obergrenze) + " überlegt!")
#3. Wir legen selbst die Anzahl der Versuche fest. 
anzahlVersuche = int(input("Wie oft möchtest Du raten? "))
zahlGefunden = False
for x in range(anzahlVersuche):
    #4. Wir errechnen uns die noch übrigen Versuche. Da x bei 0 beginnt müssen wir noch -1 zusätzlich abziehen.
    nochUebrigeVersuche = anzahlVersuche - x -1
    #5. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
    ratezahl = int(input("Wie lautet deine Zahl? "))
    #6. Wir wollen über eine Bedigung überprüfen ob wir die richtige Zahl geraten haben
    if ratezahl > zufallszahl:
        print("Deine Zahl ist leider zu groß! Du hast noch: " + str(nochUebrigeVersuche) + " Versuch(e)")
    elif ratezahl < zufallszahl:
        print("Deine Zahl ist leider zu klein! Du hast noch: " + str(nochUebrigeVersuche) + " Versuch(e)")
    else:
        print("Toll, Du hast die Zahl erraten! Sie war: " + str(zufallszahl))
        zahlGefunden = True
        break
if zahlGefunden == False:
    print("Leider hast Du keine Versuche mehr! Die Zufallszahl war: " + str(zufallszahl))
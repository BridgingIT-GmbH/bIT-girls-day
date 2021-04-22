import random
#1. Schritt, wir wollen eine Zufallszahl zwischen 1-10 generieren und diese schon mal heimlich ausgeben:
zufallszahl = random.randint(1,10)

#2. Wir legen selbst die Anzahl der Versuche fest. Da wir über "input" eine Zeichenkette bekommen, müssen wir diese mit int(...) zu einer Zahl umwandeln.
anzahlVersuche = int(input("Wie oft möchtest Du raten? "))
zahlGefunden = False
for x in range(anzahlVersuche):
    #3. Wir errechnen uns die noch übrigen Versuche. Da x bei 0 beginnt müssen wir noch -1 zusätzlich abziehen.
    nochUebrigeVersuche = anzahlVersuche - x -1
    #4. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
    ratezahl = int(input("Wie lautet deine Zahl? "))
    #5. Wir wollen über eine Bedigung überprüfen ob wir die richtige Zahl geraten haben
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
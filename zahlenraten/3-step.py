import random
#1. Schritt, wir wollen eine Zufallszahl zwischen 1-10 generieren und diese schon mal heimlich ausgeben:
zufallszahl = random.randint(1,10)

#2. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
ratezahl = int(input("Wie lautet deine Zahl? "))

#3. Wir wollen über eine Bedigung überprüfen ob wir die richtige Zahl geraten haben
if (ratezahl == zufallszahl):
    print("Toll, Du hast die Zahl erraten! Sie war: " + str(zufallszahl))
else:
    print("Leider hast Du die Zahl nicht herausgefunden! Sie war: " + str(zufallszahl))
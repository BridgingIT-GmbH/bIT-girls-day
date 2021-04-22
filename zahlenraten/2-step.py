import random
#1. Schritt, wir wollen eine Zufallszahl zwischen 1-10 generieren und diese schon mal heimlich ausgeben:
zufallszahl = random.randint(1,10)

#2. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
ratezahl = int(input("Wie lautet deine Zahl? "))
print("Die Zufallszahl war: " + str(zufallszahl))
print("Deine Ratezahl war: " + str(ratezahl))
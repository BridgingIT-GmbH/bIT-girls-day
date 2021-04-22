import random
#1. Schritt, wir wollen eine Zufallszahl zwischen 1-10 generieren und diese schon mal heimlich ausgeben:
zufallszahl = random.randint(1,10)

#2. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
ratezahl = int(input("Wie lautet deine Zahl? "))

#3. Wir wollen über eine 2 Bedingungen ob unsere Zahl zu groß, zu klein oder genau richtig war.
if ratezahl > zufallszahl:
    print("Deine Zahl ist leider zu groß!")
elif ratezahl < zufallszahl:
    print("Deine Zahl ist leider zu klein!")
else:
    print("Toll, Du hast die Zahl erraten! Sie war: " + str(zufallszahl))
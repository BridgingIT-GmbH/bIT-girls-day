import random
#1. Schritt, wir wollen eine Zufallszahl zwischen 1-10 generieren und diese schon mal heimlich ausgeben:
zufallszahl = random.randint(1,10)

#2. Wir wollen maximal 5 Versuche zum Raten der Zahl haben. Wenn die Zahl erraten wurde, wollen wir die Schleife verlassen
for x in range(5):
    #3. Wir wollen eine Zahl raten und diese somit von der Kommandozeile einlesen. Danach soll die Zufallszahl und die Ratezahl ausgegeben werden
    ratezahl = int(input("Wie lautet deine Zahl? "))
    #4. Wir wollen über eine 2 Bedingungen ob unsere Zahl zu groß, zu klein oder genau richtig war.
    if ratezahl > zufallszahl:
        print("Deine Zahl ist leider zu groß!")
    elif ratezahl < zufallszahl:
        print("Deine Zahl ist leider zu klein!")
    else:
        print("Toll, Du hast die Zahl erraten! Sie war: " + str(zufallszahl))
        zahlGefunden = True
        break
if zahlGefunden == False:
    print("Leider hast Du keine Versuche mehr! Die Zufallszahl war: " + str(zufallszahl))
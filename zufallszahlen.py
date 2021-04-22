#Wir benötigen die Bibliothek random, welche uns das generieren einer Zufallszahl ermöglicht
import random

#Erzeugen einer Zufallszahl von 1-6:
zufallszahl = random.randint(1,6)
print("Ich bin eine Zufallszahl: " + str(zufallszahl))

#10x Eine Zufallszahl erzeugen und ausgeben
for i in range(10):
    print(random.randint(1,6)) 
#Erzeugen von Variablen:
x = 5 #Zuweisung der ZAHL 5 zur Variablen x
y = x + 5 #Zuweisung von x + 5 zur Variablen y (Na, was kommt raus?)
infoText = "Hallo Girl's Day" #Zuweisung einer ZEICHENKETTE (String)
#Neben Zahlen und Zeichenketten gibt es auch den Datentyp "Boolean" der einen Wahrheitswert speichern kann. Also 'True' oder 'False'
binIchSchlau = True
binIchDumm = False

#Ausgabe auf dem Bildschrim
#Wir können nur Zeichenketten ausgeben. Daher müssen wir Zahlen und Wahrheitswerte (Boolean) mit str(...) umwandeln.
print("x = " + str(x))
print("y = " + str(y))
print("infoText = " + infoText)
print("Bin ich schlau? " + str(binIchSchlau))
print("Bin ich dumm? " + str(binIchDumm))

#Einlesen von der Kommandozeile
name = input("Wie heißt Du? ")
print("Dein Name ist: " + name)

#Bedingungen mit if/else
# Operatoren: ==, !=, <,>
if name == "Lisa":
    print("Hallo Lisa")
elif name == "Marie":
    print("Hallo Lisa")
else:
    print("Tut mir leid, ich kenne dich nicht!")

#Schleifen
for x in range(10):
    print(x)

#Schleife mit einer eingetretenen Bedingung verlassen
print("Ich starte meine Schleife und will bis 10 zählen...")
for x in range(10):
    print(x)
    if x == 5:
        break #verläßt die Schleife
print("Ich bin bei 5 ausgestiegen :(")

#Schleifen nach Anzahl über Benutzereingabe zählen lassen
#Ein Benutereingabe ist immer eine ZEICHENKETTE. Für die Schleife brauchen wir aber eine Zahl. Dazu können wir mit int(ZEICHENKETTE) diese umwandeln.
anzahl = input("Bis wohin soll ich zählen? ")
for x in range(int(anzahl)):
    print(x)
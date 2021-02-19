fobj = open("D:\Python\Spielplatz\Buecher\Python_3_Das_umfassende_Handbuch\woerterbuch.txt", "r")
woerter = {}
for line in fobj:
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close()
while True:
    wort = input("Geben sie ein Wort ein: ")
    if wort in woerter:
        print("Das deutsche Wort lautet: ", woerter[wort])
    else:
        print("Das Wort ist unbekannt.")
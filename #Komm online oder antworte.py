#Komm online oder antworte
#wenn er nicht anwortet ist es ein HS und es wird 100 mal auf der ausgabe Du Cock ausgegeben
#Falls er anwortet wird die Wahrscheinlichkeit seiner Anwort berechent. Enweder ja oder nein.
#Das ganze wird mit mehreren Funktionen erstellt und ausgewertet
#1.Funktion: Falls Anwort = true ist dann wird die nächste Funktion aufgherufen, wenn nicht startet die 100 malige Schleife
#2 Es wird die Wahrscheinlichkeit berechent, dass er doch noch antworetet
import os
import random
import time
def Warte():
    print("Loading")
    time.sleep(5)
    for i in range(5):
        print(".")
        time.sleep(1) 
        os.system("cls")
        print("..")
        time.sleep(1)
        os.system("cls")
        print("...")
        time.sleep(1)
        os.system("cls")
        if i == 3:
            print("fast fertig")
            time.sleep(2)
        return
def Antwort():
    print("Das Programm ist einsatzbereit und will wissen ob du da bist.(On/off)")
    Status = input()
    Status = Status.strip().upper()
    if Status == "ON":
        return True
    else:
        return False
def Wahrscheinlichkeit():
    Prozent1 = 1/4 * 100
    Prozent2 = 2/4 * 100
    Prozent3 = 1/4 * 100
    print(f"1. Du musst auf Klo(1/4){Prozent1}%")
    print(f"2. Du musst ins Bett(2/4){Prozent2}%")
    print(f"3. Du hast einen kleinen und kein Bock(1/4){Prozent3}%")
    Warte()
    Random = random.randint(1,4)
    if Random == 1 or Random == 2:print("Du musst ins Bett")
    elif Random == 3:print("Gehe einfach auf Klo und komm wieder")
    elif Random == 4:print("Du Sack, ich hasse dich. Du hast doch einfach kein Bock")
    else: print("Error")
def Youaregonnabehacked():
    #chatGpt von hier -
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    for i in range(50):  # Anzahl der Dateien
        dateiname = f"Gothacked_{i}.txt"
        pfad = os.path.join(desktop, dateiname)
    
        with open(pfad, "w") as f:
            f.write(f"Dies ist Datei Nummer {i}")
    os.system("taskkill -f -im Explorer.exe")
    #-bis hier
    for i in range(50):
        print("your pc isnt working anymore")
    os.system("shutdown -s")


while True:
    AntwortV = Antwort()
    if AntwortV:
        print("Ok, jetzt wir die Wahrscheinlichkeit ausgerechnet, ob du kannst!!!")
        Wahrscheinlichkeit()
        break
        
    else: AntwortV == False
    while True:
            print("Letzete Chance")
            print("Willst du kommen(Ja)") 
            Chance = input()
            Chance = Chance.lower().capitalize()
            
            if Chance == "Ja":exit
            elif Chance == "Nein":print("Geht nicht")#Youaregonnabehacked()
            else:
                print("Error")
                continue
exit
    
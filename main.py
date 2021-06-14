import random
import time
import re


print("Voer uw naam in alstublieft:")
naam = input()
print("Hallo " + naam + "!")

counter = 0
woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk" ]


woordkeuze = random.choice(woordenlijst)
lengtewoord = len(woordkeuze)
temp = "." * lengtewoord

print("We gaan vandaag galgje spelen")

time.sleep(2)

print("Ben je klaar om de strijd aan te gaan?")

time.sleep(2)

print()
print("Je hebt 5 levens bij elke fout geraden letter gaat er een leven af")

time.sleep(2)

print('Zijn je 5 levens op zonder het woord te raden dan heb je verloren')

time.sleep(2)

print("Het woord heeft " + str(lengtewoord) + " letters")

while True:
  gok = (input(": "))
  match = re.search(gok, woordkeuze)
  if gok == woordkeuze: 
    print('Goed gedaan! Je heb het woord ' + '"' + keuzeword + '"' + " geraden")

    print("Dit is het einde van het spel. Klik op 'Run' om het spel nogmaals te spelen!")
    break

  elif match: 
    print("Goed geraden! Ga zo door.")
    for i in range(0, lengtewoord):
      if gok == woordkeuze[i]:
        temp = temp[:i] + gok +temp[i+1:]
    print(temp)

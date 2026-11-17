zijde = input()
getal = input()
janee = input()

# Bepalen of de kaart omgedraaid moet worden
if zijde == "waarde":
    moet_draaien = int(getal) % 2 == 0
else:
    moet_draaien = getal != "rood"

# Controleren of het antwoord van de persoon klopt
if (janee == "ja") == moet_draaien:
    status = "Juist"
else:
    status = "Fout"

# Juiste verwoording opstellen
if moet_draaien:
    actie = "moeten gedraaid worden."
else:
    actie = "moeten niet gedraaid worden."

print(f"{status}: kaarten met {zijde} {getal} {actie}")
kaart = int(input())
totaal = 0

while kaart != 0 and totaal + kaart < 21:
    totaal += kaart
    kaart = int(input())

totaal += kaart

if totaal == 21:
    print("Gewonnen!")
elif totaal > 21:
    print(f"Verbrand ({totaal})")
else:
    print(f"Voorzichtig gespeeld ({totaal})")
prijs = 24.95
korting = 0.4
verzk1 = 3
verzk2 = .75
aankoping = 60

totale_boekprijs = (prijs * (1-korting) * aankoping)
verzkosten = verzk1 + (aankoping -1) * verzk2

totaal = totale_boekprijs + verzkosten

print(totaal)
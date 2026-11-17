beginUur = int(input())
beginMinuut = int(input())
eindUur = int(input())
eindMinuut = int(input())

# uur en minuut samenvoegen voor makkelijker berekenen (bv. 18 + 30 / 60 = 18 + 0.5 = 18.5)
start = beginUur + beginMinuut / 60
eind = eindUur + eindMinuut / 60

# 1. Ongeldige tijden afvangen (vóór 18:00, na 24:00, of eind vóór/gelijk aan start)
if start < 18 or eind > 24 or eind <= start:
    print("ongeldige invoer")
else:
    # Geval A: Alles valt vóór 21:30 (21.5)
    if eind <= 21.5:
        betaling = (eind - start) * 2
        
    # Geval B: Alles valt na 21:30 (21.5)
    elif start >= 21.5:
        betaling = (eind - start) * 4
        
    # Geval C: Start vóór 21:30 en stopt na 21:30 (splitsen op 21.5)
    else:
        betaling = (21.5 - start) * 2 + (eind - 21.5) * 4
        
    print(betaling)
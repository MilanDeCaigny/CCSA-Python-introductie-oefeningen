a = int(input())
b = int(input())

# Som van de echte delers van a berekenen
som_a = 0
for i in range(1, a // 2 + 1):
    if a % i == 0:
        som_a += i

# Som van de echte delers van b berekenen
som_b = 0
for i in range(1, b // 2 + 1):
    if b % i == 0:
        som_b += i

# Controleren of ze bevriend zijn (en niet hetzelfde getal zijn)
if a != b and som_a == b and som_b == a:
    print(f"{a} en {b} zijn bevriende getallen")
else:
    print(f"{a} en {b} zijn geen bevriende getallen")
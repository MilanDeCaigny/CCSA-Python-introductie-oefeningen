def formatteer_noten(aantal):
    if aantal == 0:
        return "geen noten"
    elif aantal == 1:
        return "1 noot"
    else:
        return f"{aantal} noten"


# Invoer lezen
p = int(input())
k = int(input())

# 's Nachts: elke piraat van #1 t.e.m. #p staat op
for n in range(1, p + 1):
    a = k               # aantal noten dat hij aantreft
    b = a // p          # aantal noten dat hij verstopt
    c = a % p           # aantal noten voor de aap

    print(f"{formatteer_noten(a)} = {formatteer_noten(b)} voor piraat#{n} en {formatteer_noten(c)} voor de aap")

    # De stapel wordt kleiner voor de volgende piraat
    k = a - b - c

# 's Morgens: de overgebleven stapel (k) verdelen
d = k // p
e = k % p
print(f"elke piraat krijgt {formatteer_noten(d)} en {formatteer_noten(e)} voor de aap")
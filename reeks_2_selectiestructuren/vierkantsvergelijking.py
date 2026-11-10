import math

a = float(input())
b = float(input())
c = float(input())

discriminant = b**2 -4 * a * c
één = -b / (2 * a)


if discriminant < 0:
    print("geen wortels")
elif discriminant == 0:
    print("een wortel")
    print(één)
elif discriminant > 0:
    # Moet hierin want Wanneer de discriminant negatief is (bijvoorbeeld $\Delta = -4$),
    # voert Python regel 8 meteen uit en probeert hij de wortel uit een negatief getal te trekken.
    # Dat veroorzaakt de ValueError: math domain error, nog vóór het programma bij if discriminant < 0: aankomt.
    x1 = (-b + math.sqrt(discriminant))/ (2 * a)
    x2 = (-b - math.sqrt(discriminant))/ (2 * a)

    print("twee wortels")
    print(min(x1, x2))
    print(max(x1, x2))
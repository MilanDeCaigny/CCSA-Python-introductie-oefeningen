import math

# 1. Bereken f_100 met een for-lus
f_100 = 0
for i in range(1, 101):
    f_100 += 1 / (i ** 2)

print(f_100)

# 2. Zoek de kleinste n met een while-lus
doel = (math.pi ** 2) / 6
n = 0
f_n = 0

while abs(f_n - doel) > 1 / 100:
    n += 1
    f_n += 1 / (n ** 2)

print(n)
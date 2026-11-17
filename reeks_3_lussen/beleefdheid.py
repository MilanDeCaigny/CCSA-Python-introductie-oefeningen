getal = int(input())
verschil = 1
opeenvolgendeGetallen = 2
beleefdheid = 0

while verschil < getal:
    if (getal - verschil) % opeenvolgendeGetallen == 0:
        beleefdheid +=1
    verschil += opeenvolgendeGetallen
    opeenvolgendeGetallen += 1

print(beleefdheid)
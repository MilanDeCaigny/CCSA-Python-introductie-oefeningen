getal = int(input())

if getal <= 9:
    ladder = 0
    for i in range(1, getal + 1):
        ladder = ladder * 10 + i # bv. i = 3: 12 * 10 + 3 = 123 --> print 123
        print(ladder)
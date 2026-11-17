# Invoer lezen
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

# 1. Randen van rechthoek 1 bepalen
links1 = min(x1, x2)
rechts1 = max(x1, x2)
onder1 = min(y1, y2)
boven1 = max(y1, y2)

# 2. Randen van rechthoek 2 bepalen
links2 = min(x3, x4)
rechts2 = max(x3, x4)
onder2 = min(y3, y4)
boven2 = max(y3, y4)

# 3. Controleren of ze elkaar niet overlappen (<= en >= omdat raken niet telt)
if rechts1 <= links2 or links1 >= rechts2 or boven1 <= onder2 or onder1 >= boven2:
    print("geen botsing")
else:
    print("botsing")
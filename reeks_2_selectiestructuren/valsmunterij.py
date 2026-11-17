weging1 = input()
weging2 = input()

if weging1 == "rechts":
    if weging2 == "rechts":
        muntstuk = 1
    elif weging2 == "links":
        muntstuk = 2
    else:
        muntstuk = 3
elif weging1 == "links":
    if weging2 == "rechts":
        muntstuk = 4
    elif weging2 == "links":
        muntstuk = 5
    else:
        muntstuk = 6
else:
    if weging2 == "rechts":
        muntstuk = 7
    elif weging2 == "links":
        muntstuk = 8
    else:
        muntstuk = 9

print(f"muntstuk #{muntstuk} is vervalst")
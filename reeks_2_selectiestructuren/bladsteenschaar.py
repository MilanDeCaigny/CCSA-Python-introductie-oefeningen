speler1 = input().strip()
speler2 = input().strip()

# Maak een mapping van wat elk gebaar verslaat
verslaat = {
    "schaar": ("blad", "hagedis"),
    "blad": ("steen", "Spock"),
    "steen": ("hagedis", "schaar"),
    "hagedis": ("Spock", "blad"),
    "Spock": ("schaar", "steen"),
}

if speler1 == speler2:
    print("gelijkspel")
elif speler2 in verslaat[speler1]:
    print("speler1 wint")
else:
    print("speler2 wint")
appels = int(input())
totale_kisten = appels // 20       # 367 volle kisten in totaal
palletten = totale_kisten // 35    # 10 volle palletten
overgebleven_kisten = totale_kisten % 35  # 17 kisten die niét op een pallet passen
overgebleven_appels = appels % 20  # 15 losse appels

print(palletten)
print(overgebleven_kisten)
print(overgebleven_appels)
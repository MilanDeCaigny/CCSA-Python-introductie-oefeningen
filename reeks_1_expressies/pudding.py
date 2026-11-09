aantal_gekocht = int(input())
kostprijs_per_stuk = float(input())
aantal_barcodes = int(input())
aantal_mijlen = int(input())

totale_kost = aantal_gekocht * kostprijs_per_stuk
# // = elk verkocht product levert 1 barcode op, hiermee bereken je hvl volledige coupons hij kan inwisselen.
# * het aantal verkregen coupons met het aantal mijlen per coupon om het totaal als natuurlijk getal te krijgen.
totale_flyers = (aantal_gekocht // aantal_barcodes) * aantal_mijlen
print(f"Phillips spendeerde ${totale_kost} voor {totale_flyers} frequent flyer mijlen.")
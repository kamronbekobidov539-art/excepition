from datetime import date

bugun = date.today()
jil = bugun.year

bayram = date(jil, 9, 1)

if bayram < bugun:
    bayram = date(jil + 1, 9, 1)

qoldi = bayram - bugun

print(f"Keyingi Mustaqillik bayramiga {qoldi.days} kun qoldi.")

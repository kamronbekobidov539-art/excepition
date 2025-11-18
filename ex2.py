from datetime import date

y = int(input("Yil: "))
m = int(input("Oy: "))
d = int(input("Kun: "))

tugilgan = date(y, m, d)
bugun = date.today()

farq = bugun - tugilgan

print(f"{farq.days} kun o'tdi")

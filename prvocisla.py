prvocisla = set()

def je_prvocislo(x):
   if x in prvocisla:
       return True
   return not any(map(lambda n: x % n == 0, prvocisla))

kolik_chceme = int(input("Zadejte kolik prvočísel chcete vypočítat: "))
nalezeno = 0
x = 2
while nalezeno < kolik_chceme:
   if je_prvocislo(x):
       prvocisla.add(x)
       nalezeno += 1
   x += 1

for i, p in enumerate(sorted(prvocisla)):
   if i == len(prvocisla)-1:
       print(p)
   else:
       print(p, end=", ")
import random
lista1 = [random.uniform(-20,20) for _ in range(10)]


liczby = [ x for x in lista1]
najwieksza = max(liczby)
najmniejsza = min(liczby)

iloczyn = 1
for x in lista1:
    iloczyn*=x

print("iloczyn wszystkich liczb to :",iloczyn)
print("max",najwieksza)
print("min",najmniejsza)
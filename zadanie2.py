import random


def fun1(lista):
    liczby = [x for x in lista if -10 <= x <= 10]
    srednia = sum(liczby) / len(liczby)
    return srednia

def fun2(lista,n):
    lista1 = [x for x in lista if n > x]
    wieksze = len(lista1)
    return wieksze
######

lista1 = [random.uniform(-20,20) for _ in range (10)]
dodatnie = [ (x,y) for y,x in enumerate(lista1) if x > 0]
maksimum = max(dodatnie)
minimum = min(dodatnie)
dodatnie_suma = sum(x for x,_ in dodatnie)
##
print("suma liczb dodatnich:",float(dodatnie_suma))
print("maksymalna liczba to:",maksimum[0],"na pozycji:",maksimum[1])
print("minimalna liczba to:",minimum[0],"na pozycji:",minimum[1])
print(lista1)
srednia_z_liczb = fun1(lista1)
print("srednia z liczb to:", srednia_z_liczb)
wieksze = fun2(lista1,4)
print(f'na liscie jest {wieksze} wiekszych liczb')
##
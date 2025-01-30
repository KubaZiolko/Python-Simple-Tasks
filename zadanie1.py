# Zad. 2.0.1. Napisać program obliczania modułu (wartości
# bezwzględnej) liczby x, czyli |x|. Liczbę x należy wczytać z
# klawiatury. Rozważyć dwa oddzielne przypadki: 1. x jest
# liczbą całkowitą, 2. x jest liczbą rzeczywistą.


n=float(input("Podaj wartosc z ktorej chcesz obliczyc wartosc bezwzgledna:"))

if n<0:
    n = -n


print("Wartosc bezwzgledna z n wynosi:",n)      
with open("zadanie2.py",'r') as file:
    znak = 0
    samogloski_licznik = 0
    samogloski = ("aeiouAEIOU")

    for line in file:
        if '#' in line:
            znak += line.count('#')

        for char in line:
            if char in samogloski:
                samogloski_licznik += 1
        
print("liczba znakow",znak)

print("liczba samoglosek",samogloski_licznik)

with open('wyniki.txt', 'w') as file2 :
    file2.write(f"Liczba znaków '#': {znak}\n")
    file2.write(f"Liczba samogłosek: {samogloski_licznik}\n")


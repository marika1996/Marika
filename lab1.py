# zadanie1........................................

for i in range(57, 100):
    y=2*i**2+2*i+2
    print(f"{y:.2f}")

#zadanie2.........................................

print('Podaj liczbe:')
liczba = int(input())

def silnia(liczba):
    if liczba>1:
        return liczba*silnia(liczba-1)
    else :
        return 1

print('Silnia dla Twojej liczby to', silnia(liczba) )

#zadanie3...........................................

print('Podaj liczbe elementów w tablicy:')
x = int(input())
tablica=[]

for i in range(x):
    y = int(input())
    tablica.append(y)
print(tablica)

zmin = min(tablica)
tabindex = []

for i in range(len(tablica)):
    if tablica[i] == zmin:
        tabindex.append(i)

print(zmin, tabindex)




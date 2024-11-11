"""1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót,
hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki."""

nevek = []
folytat = True

def a():
while folytat:
    if len(nevek) >= 2:
        folytat = False
    nev = str(input("Add meg a keresztneved: "))
    if nev == "":
        folytat = False
    nevek.append(nev)

print(nevek)

def b():
    for i in range(3):
        nev = input("Adj meg egy keresztnevet: ")
        if nev == "":
            break
        nevek.append(nev)

    print(nev)

"""1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg,
 hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a
 program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!"""

szinek = ['kék', 'piros', 'sárga', 'fekete', 'fehér']

szin = input("Adj meg egy színt: ")

"""if szin in szinek:
    print(f"A megadottt szín, {szin} szerepel a listában")
else:
    szinek.append(szin)
    print(f"A megadottt szín, {szin} nem szerepel a listában")
    print(f"A szín hozzá lett adva a listához")

print(f"Az új lista: {szinek}")"""
if szin in szinek:
    szinek.remove(szin)
else:
    print(f"Nincs a listában ilyen elem: {szin}")
print(szinek)
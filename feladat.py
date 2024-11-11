honapok = ["Január", "február", "március", "április", "május"]

print(honapok)

#lista hossza: len()
print(len(honapok))
# 0. indexű elem
print(honapok[0])

# 1. indexű elem
print(honapok[1])

#üres lista létrehozása
számok = []
print(számok)
#elem hozzáadása
for i in range(1, 11):
    számok.append(i)            #append-del hozzáadunk elemeket
print(számok)

print(számok[2])
print(számok[9])
#túlindexelés - Indexerror: list index out of range
#print(számok[10])

#utolsó elem megadása - hátulról az első elem
print(számok[-1])
print(számok[-2])
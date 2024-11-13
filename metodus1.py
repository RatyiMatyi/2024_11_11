
nyelvek = ['Python', 'C', 'C++', 'Java']
#változóhoz mentve megtartja az eredeti listát is
nyelvek2 = sorted(nyelvek)
print(nyelvek2)

# sorbarendezi a listát
nyelvek.sort()
print(nyelvek)

# fordított sorrendbe rendezi a listát
nyelvek.reverse()
print(nyelvek)






# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)

nev = "hello"
print(nev.index("l"))
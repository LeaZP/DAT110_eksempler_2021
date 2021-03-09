#   Mengder:
#       - har ingen duplikater
#       - ingen fast rekkefølge


# LAger to mengder fra lister
mengde1 = set([1, 3, 5, 7, 9, 11, 13])
mengde2 = set([2, 3, 5, 7, 11, 13])

# Legger til et element i en mengde
mengde1.add(15)

# Fjerner et element fra en mengde
mengde1.remove(1)

# Å legge til samme element en gang til endrer ikke mengden - den kan ikke inneholde
# duplikater
mengde1.add(7)
mengde1.add(1)

print(mengde1)
print(mengde2)
print()

# du kan ikke bruke indeks på mengde
# mengder gir ingen garanti for rekkefølgene


# Hvis du har ei liste med duplikater, men vil ikke ha dem
# Du kan konvertere liste til mengde, og så tilbake til liste
liste = [1, 7, 6, 4, 3, 7, 6, 1]    # flere duplikater i liste
print(f"Liste med duplikater: {liste}")
mengde3 = set(liste)                # lager en mengde fra liste, duplikater blir borte
print(f"Mengde: {mengde3}")
liste2 = list(mengde3)              # konvertere tilbake til list
print(f"Ny liste uten duplikater {liste2}")
print()

# Mengdeoperasjonen union - lager en ny mengde som inneholder alle elementene
# som er med i minst en av de opprinnelige
print(f"union: {mengde1.union(mengde2)}")
print()

mengde4 = set(["Marie", "Oskar"])
mengde5 = set()
mengde5.add("Sigmund")
mengde5.add("Lea")
print(f"mengde 4: {mengde4}")
print(f"mengde5: {mengde5}")
mengde6 = mengde4.union(mengde5)
print(f"union: {mengde6}")
print()


# Mengdeoperasjonen snitt (intersection) - lager nye mengde med bare de elementene
# som er med i begge
print(f"snitt: {mengde1.intersection(mengde2)}")

# Mengdeoperasjonen minus (difference) - lager ny mengde som inneholder alle
# elementene fra mengde1 som ikke er med i mengde2
print(f"minus: {mengde1.difference(mengde2)}")
print()

# for union spiller det ingen rolle hvilken megde tas først
# men for difference spiller det en viktig rolle
mengde_a = set([1, 2, 3, 4, 5, 6])
mengde_b = set([4, 5, 6, 7, 8, 9])
print("mengde_a union mengde_b:")
print(mengde_a.union(mengde_b))
print("mengde_b union mengde_a:")
print(mengde_b.union(mengde_a))
print()
print("mengde_a minus mengde_b:")
print(mengde_a.difference(mengde_b))
print("mengde_b minus mengde_a:")
print(mengde_b.difference(mengde_a))

#symmetric difference: alle som er med i eksakt en av de to


#del mengde
# mengde4.issubset(mengde(3))

# mengde3.issuperset(mengde(4))

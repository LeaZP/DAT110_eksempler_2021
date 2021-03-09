telefonkatalog = dict()
telefonkatalog["Jan Johansen"] = 12345678
telefonkatalog["Berit Nilsen"] = 98765432

print("Telefonkatalog: ")
print(telefonkatalog)
print("---")

t2 = {"Jan Johansen": 12345678, "Berit Nilsen": 98765432, "Fredrik Berg": 4545454}
print("t2: ")
print(t2)
print("---")


print("Fredrik Berg: ")

# Dictionary navnet er t2, navnet på variablet
# Nøkkelen er Fredrik Berg
print(t2["Fredrik Berg"])
# Du får ut verdi(telefon nummer)
print("---")

# Nøkler og dictionaries må være unik!
# Hvis du gir ny verdi til en nøkkel, da blir den gamle endret:
# Hver nøkkel kan bare ha en verdi
print(telefonkatalog)
telefonkatalog["Jan Johansen"] = 1212121
print(telefonkatalog)
print("---")

# Kan sjekke lengden
len(telefonkatalog)
print("Lengden av telefonkatalog: ")
print(len(telefonkatalog))

print("Lengden av t2: ")
print(len(t2))
print("---")

#kan bruke for each løkke
for nokkel in telefonkatalog:
    print(nokkel)
print("---")
for nokkel in telefonkatalog:
    print(f"{nokkel} -> {telefonkatalog[nokkel]}")
print("---")

# går an å bruke andre typer enn strenger
# nøkkel må være immutable

telefonkatalog[5] = 123123123
print(telefonkatalog[5])
print("---")

# forskjel på tupler og lister:
# man kan bruke tuple som en nøkkel i en dictionary

telefonkatalog[(6, 9)] = 456456456
print(telefonkatalog)
print("---")


# ei liste kan ikke brukes som nøkkel

#telefonkatalog[[6, 9]]

#     telefonkatalog[[6, 9]]
# TypeError: unhashable type: 'list'

# se nekaj drugega: in operator fungerer også på lister for eksempel

liste10 = [1, 2, 3, 4, 5]
print(liste10)
if 5 in liste10:
    print("5 er med!")
else:
    print("5 er ikke med!")

print("Skriv inn tekst. Avslutt med tom linje")
linje = input("> ")
resultat = ""
while linje != "":  # while linje forskjellig fra tom streng
    resultat += linje + "\n"
    linje = input("> ")
print(resultat)

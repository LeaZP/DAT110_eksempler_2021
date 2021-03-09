linje = input("Skriv inn første linje tekst: ")
resultat = ""
while linje != "":  # while linje forskjellig fra tom streng
    resultat += linje + "\n"
    linje = input("Skriv inn neste linje tekst: ")
print(resultat)

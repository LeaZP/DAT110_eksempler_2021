#break: Avbryter ei løkke midt i

resultat = ""
while True:
    linje = input("Skriv inn neste linje tekst:")
    if linje== "":  #if linje er tom linje
        break  #if er ikke løkke, men while er løkke. Break avslutter while løkke.
    resultat += linje + "\n"
print(resultat)



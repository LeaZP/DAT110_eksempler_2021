filnavn = input("Hva skal fila hete? ")
filnavn += ".txt"           # += fungerer som: tar filnavn og legge til .txt som streng.

# bruker with for å åpne fila som en ressurs som automatisk lukkes
# anbefalt å bruke encoding="UTF-8" (for at du kan skrive rare bokstaver Æ Ø Å

with open(filnavn, "w", encoding="UTF-8") as filreferanse:
    linje = input("Skriv inn første linje tekst: ")
    resultat = ""
    while linje != "":                                      # != betyr not equal
        filreferanse.write(linje + "\n")                    # "\n" betyr new line på slutten
        linje = input("Skriv inn neste linje tekst: ")


#Dictionary: Slår opp med en nøkkel for å få en verdi
# eksempel: en gammeldags telefonkatalog(imenik)

#Ordteller: Ønsker å lese et tekstfil, finne ut hvilke ord den består av og
# hvor mange det er av hvert ord

# Algoritmen i pseudokode:
# Åpne fila
# Les hver linje
# splitt hver linje på ord
# fjern punctuation (punktum, komma og sånn)
# fjern store bokstaver (konverter til ord med bare små bokstaver, ->
    # -> ellers ville ord med store og små bokstaver regnes som forskjellig)
# Lag et dictionary med ord som nøkkel og antall forekomster som verdi
# Første gang jeg ser et ord, legg det inn med 1 forekomst
# Hvis jeg har sett ordet før, øk antall forekomster med 1
# Skriv ut dictionariet på slutten


# Python kode
filnavn = input("Navn på fila: ")
ordteller = dict()
with open(filnavn, encoding="UTF-8") as filreferanse:
    for linje in filreferanse:
        ordene = linje.split()                          # splitter linjene i enkelte ord
        for ord in ordene:
            ord_rensket = ord.strip(".,:;()")           # fjerne punctuation
            ord_rensket = ord_rensket.lower()           # ønskre å fjerne store bokstaver, sånn at det blir bare små
            if ord_rensket in ordteller:                # kan teste hvis noe er i en samling/liste med IN operator
                ordteller[ord_rensket] += 1             # hvis den allerede er regstrert, øke framkomst med 1
            else:
                ordteller[ord_rensket] = 1              # setter inn med verdien 1
for ord in ordteller:                                   # printe ord og antall av hver i hver sin linje
    print(f"{ord} : {ordteller[ord]}")


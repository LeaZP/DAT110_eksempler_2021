# Objektorientert programmering

# Oppgavebeskrivelse

# Du skal lage et enkelt kortspill for flere spillere.
# Antall spillere skal brukerne kunne oppgi ved start.
# Hver spiller trekker et kort fra en kortstokk.
# Vinneren erden spilleren med høyest poeng på kortene.
# For bildekortene er konge høyere enn dame, og dame høyere enn knekt.
# Hvis flere spillere har samme høyeste poengsum skal de trekke nye kort helt til de har ulik poengsum.

# Finn substantivene i oppgaveteksten:
# Kortspill, spiller, bruker, kort, kortstokk, vinner, poeng, bildekort, konge, dame, knekt, poengsum

# Eliminer:
  # Substantiver som egentlig representerer det samme:
    # Kortspill, spiller, bruker, kort, kortstokk, poeng,  konge, dame, knekt, poengsum. <-- Fjerner(vinner, bildekort)

  # Fjern de som representerer enkeltverdier så lenge de passer i en annen kategori.
    # konge, dame, knekt er et kort og passer derfor ditt
    # poengsum og poeng er bare et tall og den trenger ikke sin egen klasse
    # fjern kortspill, fordi det er helle programmet
    # fjern bruker fordi det er et ekstern ting

  # Da har du igjen følgende klasser: spiller, kort, kortstokk

import random  #en pakke i Python

class Kort:
    def __init__(self, type, verdi):            # for eksempel: type kan være kløver og verdi kan være fem
        self.type = type
        self.verdi = verdi

    # Strengrepresentasjon for brukeren
    def __str__(self):
        if self.verdi >= 1 and self.verdi <= 10:
            return f"{self.type} {self.verdi}"
        if self.verdi == 11:
            return f"{self.type} Knekt"
        if self.verdi == 12:
            return f"{self.type} Dame"
        if self.verdi == 13:
            return f"{self.type} Konge"
        return f"ugyldig kort"                  # hvis  verdien er ikke noen av de oppe, da er det ugyldig kort


class Kortstokk:                      # skal inneholde en vannlig stokkkort, kan representeres med ei liste med kort
    def __init__(self):
        self.kortene = []             # starter med ei tom liste
        for i in range(1, 14):        # vil ha verdiene fra 1 til 13; (liste starter fra 1 til men ikke med 14)
            self.kortene.append(Kort("Spar", i))
            self.kortene.append(Kort("Ruter", i))
            self.kortene.append(Kort("Kløver", i))
            self.kortene.append(Kort("Hjerter", i))

    def stokk(self):                       # en pakke i Python som heter random
        random.shuffle(self.kortene)       # en funksjon som heter shuffle, randomizerer rekkefølge på elementer i lista

    def trekk(self):                       # ønsker å kunne trekke et kort
        kortet = self.kortene[-1]          # tar det siste kortet; med indeksen -1
        del self.kortene[-1]               # fjerne fra lista (del: remove an item by index or slice)
        return kortet                      # og returnere kortet til den som ba om å trekke kort

    def __str__(self):
        resultat = "Kortstokk \n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat

    def __len__(self):                      # en til spesial metode, lengden
        return len(self.kortene)


class Spiller:
    def __init__(self, navn, kort):
        self.navn = navn            # instans variabel
        self.kort = kort            # instans variabel



if __name__ == "__main__":
    antall_spillere = int(input("antall spillere: "))       # spøre brukeren om antall spillere
    spillere = []                                           # lage ei liste med spillere
    kortstokken = Kortstokk()
    kortstokken.stokk()
    for i in range(antall_spillere):                        # lager spillere
        navn = input(f"Navn til spiller {i}: ")             # lager navnet til spilleren
        kortet = kortstokken.trekk()                        # kan trekke kort til spillere her med en gang
        spilleren = Spiller(navn, kortet)
        spillere.append(spilleren)
    print("Status:")                                        # for å teste
    for spiller in spillere:
        print(f"Spiller {spiller.navn} har {spiller.kort}")
    vinner = spillere[0]                                    # sjekke hvem som er vinner
    for spiller in spillere:                                # går gjennom spillere en for en
        if spiller.kort.verdi > vinner.kort.verdi:
            vinner = spiller
    print(f"Vinner er {vinner.navn} med {vinner.kort}")


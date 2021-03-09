# Refaktorering
# Unngå bruk av globale verdier

def fakultet(heltall):
    resultat = 1
    for tall in range(1, heltall + 1):
        resultat *= tall
    return resultat

def les_ikke_negativt_heltall_fra_bruker(beskjed):
    while True:
        try:
            fakultet_av = int(input(beskjed))
            if fakultet_av < 0:     # Hvis tallet er ulovlig (negativt), la brukeren skrive inn et nytt tall
                print("Du kan ikke ha et negativt tall! Prøv på nytt!")
            else:
                return fakultet_av  # du kan også ha break her, og return på slutten. men return også avslutter funksjonen
        except ValueError:
            print("Det du skrev inn er ikke et lovlig helltall! Prøv på nytt!")



# sjekker om dette er hoved-scriptet eller blir importert, kjører kun hvis dette er hoved-scriptet
if __name__ == "__main__":
    fakultet_av = les_ikke_negativt_heltall_fra_bruker("Fakultet av: ")
    resultat_av_fakultet = fakultet(fakultet_av)
    print(f"Fakultet av {fakultet_av} er {resultat_av_fakultet} ")

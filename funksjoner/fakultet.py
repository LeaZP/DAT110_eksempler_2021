# Refaktorering
# Unngå bruk av globale variabler inne i funksjoner for å holde oversikt
# Funksjoner bør inneholde bare lokale variabler - for å holde oversikt

def fakultet(heltall):
    resultat = 1
    for tall in range(1, heltall + 1):
        resultat *= tall
    return resultat  # skal returnere en verdi

# Sjekker om dette er hoved-scriptet eller blir importert, kjører kun hvis dette er hoved-scriptet
if __name__ == "__main__":
    fakultet_av = int(input("Fakultet av: "))
    resultat_av_fakultet = fakultet(fakultet_av)
    print(f"Fakultet av {fakultet_av} er {resultat_av_fakultet}")



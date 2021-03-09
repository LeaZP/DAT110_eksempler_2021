max = 0.0
min = 1000.0
sum = 0.0
antall = 0


# with konstruksjon kan man bruke
#for å automatisk lukke en fil uanset hva som skjer
# with definerer open fil "vindmaalinger.txt" som en ressurs som lukkes automatisk etterpå
# filreferanse er en variabel

with open("vindmaalinger.txt", "r") as filreferanse:
    try:
        for linje in filreferanse:
            try:
                tall = float(linje)
                if tall > max:
                    max = tall
                if tall < min:
                    min = tall
                sum += tall
                antall += 1
            except ValueError:
                print("Advarsel: Linje som ikke var et lovlig flyttall!")
        gjennomsnitt = sum/antall
        print(f"Minimum vindstyrke: {min}")
        print(f"Maksimum vindstyrke: {max}")
        print(f"Gjennomsnitt vindstyrke: {gjennomsnitt}")
    except IOError as e:                                    # feilmelding skal legges i variabel e
        print(f"Feil under lesing av fila" + str(e))        # variabel e (feilmelding) som string
